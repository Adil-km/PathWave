from django.db import models

# Create your models here.
class Upload(models.Model):
    discription = models.TextField(max_length=100)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return f"{self.image.name}"
