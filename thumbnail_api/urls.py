from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListImagesView.as_view(), name='list_images'),
    path('upload/', views.UploadImageView.as_view(), name='upload_image'),
    path('expiring-link', views.CreateExpiringLinkAPIView.as_view(), name='generate_link'),
    path('expiring-link/<str:signed_link>/', views.ExpiringLinkDetailAPIView.as_view(), name='expiring_link'),
]
