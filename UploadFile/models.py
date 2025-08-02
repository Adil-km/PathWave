from django.db import models

class Upload(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    original_image = models.ImageField(upload_to="images/")
    generated_audio = models.FileField(upload_to="audio/")


    def __str__(self):
        return f"{self.original_image.name} -> {self.generated_audio.name}"
