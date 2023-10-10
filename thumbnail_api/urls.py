from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListImagesView.as_view()),
    path('upload/', views.UploadImageView.as_view()),
    path('thumbnail200/<int:pk>/', views.GetThumbnail200View.as_view()),
    path('thumbnail400/<int:pk>/', views.GetThumbnail400View.as_view()),
    path('<int:pk>/', views.GetOriginalImageView.as_view()),

]