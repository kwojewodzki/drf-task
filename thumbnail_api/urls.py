from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListImagesView.as_view()),
    path('upload/', views.UploadImageView.as_view())
]