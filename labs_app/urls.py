from django.urls import path
from .views import EnhanceImageView

urlpatterns = [
    path('enhance-image/', EnhanceImageView.as_view(), name='enhance_image'),
]