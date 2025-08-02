from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('upload/', views.UploadImage, name="upload"),
    path('gallery/', views.viewGallery, name="gallery"),
    path('image/<int:id>/', views.imageDetail, name='image_detail'),
]
