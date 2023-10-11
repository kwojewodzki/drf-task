from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListImagesView.as_view()),
    path('upload/', views.UploadImageView.as_view()),
    path('expiring_link', views.CreateExpiringLinkAPIView.as_view()),
    path('expiring-link/<str:signed_link>/', views.ExpiringLinkDetailAPIView.as_view(), name='expiring_link'),
]
