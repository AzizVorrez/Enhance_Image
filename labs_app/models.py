from django.db import models

class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/')
    enhanced_image = models.ImageField(upload_to='enhanced_images/', null=True, blank=True)