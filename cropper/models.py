
from django.db import models
from .validators import validate_file_size

class Photo(models.Model):
    file = models.ImageField(validators=[validate_file_size])
    description = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'photo'
        verbose_name_plural = 'photos'

