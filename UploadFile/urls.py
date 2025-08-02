from django.urls import path, include
from . import views

urlpatterns = [
    path('upload/', views.UploadImage, name="UploadImage"),
]
