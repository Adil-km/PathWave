from PIL import Image
import numpy as np
import wave
import struct
import os
from django.conf import settings

sample_rate = 44100
step_duration = 0.32  # seconds per column

# Musical notes from C4 to B5
note_scale = [
    261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88,  # C4 to B4
    523.25, 587.33, 659.25, 698.46, 783.99, 880.00, 987.77   # C5 to B5
]

def generate_tone(freq, duration, volume=1.0):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    tone = np.sin(2 * np.pi * freq * t) * volume
    tone += 0.5 * np.sin(2 * np.pi * freq * 2 * t) * volume  # 2nd harmonic
    tone += 0.3 * np.sin(2 * np.pi * freq * 3 * t) * volume  # 3rd harmonic

    # Envelope for smooth in/out
    fade_len = int(0.01 * sample_rate)
    envelope = np.ones_like(tone)
    envelope[:fade_len] = np.linspace(0, 1, fade_len)
    envelope[-fade_len:] = np.linspace(1, 0, fade_len)
    return tone * envelope

def add_reverb(audio, delay_ms=120, decay=0.4, repeats=4):
    delay_samples = int(sample_rate * (delay_ms / 1000.0))
    output = np.copy(audio)

    for i in range(1, repeats + 1):
        delayed = np.zeros_like(audio)
        start = delay_samples * i
        if start < len(audio):
            delayed[start:] = audio[:-start] * (decay ** i)
            output += delayed

    return output / (np.max(np.abs(output)) + 1e-9)

def image_to_music(image_path, output_path=None):
    image = Image.open(image_path).convert("L")  # Grayscale
    columns = 64
    rows = len(note_scale)
    image = image.resize((columns, rows))
    pixels = np.asarray(image) / 255.0  # Normalize

    total_samples = int(columns * step_duration * sample_rate)
    audio = np.zeros(total_samples)

    for x in range(columns):
        start = int(x * step_duration * sample_rate)
        end = start + int(step_duration * sample_rate)
        slice_audio = np.zeros(end - start)

        notes_with_volume = []
        for y in range(rows):
            brightness = pixels[y, x]
            if brightness > 0.2:
                volume = brightness * 0.5
                notes_with_volume.append((note_scale[y], volume))

        notes_with_volume.sort(key=lambda nv: nv[1], reverse=True)
        for freq, vol in notes_with_volume[:3]:
            tone = generate_tone(freq, step_duration, vol)
            slice_audio[:len(tone)] += tone

        slice_audio /= np.max(np.abs(slice_audio)) + 1e-9
        audio[start:start + len(slice_audio)] += slice_audio

    audio = add_reverb(audio, delay_ms=150, decay=0.5, repeats=6)
    audio /= np.max(np.abs(audio)) + 1e-9

    # ✅ Save to output path (passed from view)
    if output_path is None:
        output_path = os.path.join(settings.MEDIA_ROOT, "audio", "music_output.wav")
    else:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with wave.open(output_path, 'w') as f:
        f.setnchannels(1)
        f.setsampwidth(2)  # 2 bytes = 16-bit
        f.setframerate(sample_rate)
        f.writeframes(b''.join(struct.pack('<h', int(s * 32767)) for s in audio))

    print("✅ Generated:", output_path)
