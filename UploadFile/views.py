import os
import uuid
import cv2
import numpy as np
from django.shortcuts import render, redirect
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.conf import settings
from django.urls import reverse
from .models import Upload
from .convertToAudio import image_to_music


def custom_stroke_extraction_save(img_path, output_path,
                                   stroke_thickness=2,
                                   stroke_color=(255, 255, 255),
                                   background_color=(0, 0, 0),
                                   blur_strength=9,
                                   block_size=15,
                                   c_value=5):
    img = cv2.imread(img_path)
    if img is None:
        return False
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (blur_strength, blur_strength), 0)
    edges = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                  cv2.THRESH_BINARY, block_size, c_value)
    strokes = cv2.bitwise_not(edges)

    if stroke_thickness > 1:
        kernel = np.ones((stroke_thickness, stroke_thickness), np.uint8)
        strokes = cv2.dilate(strokes, kernel, iterations=1)

    h, w = strokes.shape
    canvas = np.full((h, w, 3), background_color, dtype=np.uint8)

    for y in range(h):
        for x in range(w):
            if strokes[y, x] > 10:
                canvas[y, x] = stroke_color

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    cv2.imwrite(output_path, canvas)
    return True


def UploadImage(request):
    if request.method == "POST" and request.FILES.get("image"):
        uploaded_file = request.FILES["image"]
        file_id = str(uuid.uuid4())

        # Save original image to media/images/
        image_name = f"{file_id}.png"
        image_rel_path = os.path.join("images", image_name)
        saved_path = default_storage.save(image_rel_path, ContentFile(uploaded_file.read()))
        image_abs_path = default_storage.path(saved_path)

        # Processed stroke path (temporary)
        processed_rel_path = os.path.join("temp", f"processed_{file_id}.png")
        processed_abs_path = default_storage.path(processed_rel_path)
        custom_stroke_extraction_save(image_abs_path, processed_abs_path)

        # Output audio path
        audio_name = f"{file_id}.wav"
        audio_rel_path = os.path.join("audio", audio_name)
        audio_abs_path = os.path.join(settings.MEDIA_ROOT, audio_rel_path)
        os.makedirs(os.path.dirname(audio_abs_path), exist_ok=True)

        # Generate music from processed image
        image_to_music(processed_abs_path, output_path=audio_abs_path)

        # Cleanup temporary file
        if os.path.exists(processed_abs_path):
            os.remove(processed_abs_path)

        # Save both paths in DB
        obj = Upload.objects.create(
            original_image=image_rel_path,
            generated_audio=audio_rel_path
        )

        # Redirect to avoid resubmission on refresh
        return redirect(reverse("upload") + f"?id={obj.id}")

    # Handle GET (render page and show result if redirected)
    context = {}

    image_id = request.GET.get("id")
    if image_id:
        try:
            obj = Upload.objects.get(id=image_id)
            context["success"] = True
            context["image_path"] = obj.original_image.url
            context["audio_path"] = obj.generated_audio.url
        except Upload.DoesNotExist:
            pass

    context["items"] = Upload.objects.order_by("-uploaded_at")[:10]
    return render(request, "upload.html", context)

def viewGallery(request):
    context = {}

    image_id = request.GET.get("id")
    if image_id:
        try:
            obj = Upload.objects.get(id=image_id)
            context["success"] = True
            context["image_path"] = obj.original_image.url
        except Upload.DoesNotExist:
            pass

    context["items"] = Upload.objects.all()
    return render(request, 'gallery.html', context)