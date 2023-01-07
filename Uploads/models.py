from django.db import models

class File(models.Model):
    objects = models.Manager()
    Title = models.CharField(max_length=255, blank=True)
    File = models.FileField(upload_to="")
    uploaded_at = models.DateTimeField(auto_now_add=True)

# Create your models here.
