from django.db import models

# Create your models here.
class Photo(models.Model):
    # image = models.ImageField(upload_to='images/', width_field='picture_width', height_field='picture_height', max_length=255, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    image = models.CharField(max_length=255, null=True, blank=True)