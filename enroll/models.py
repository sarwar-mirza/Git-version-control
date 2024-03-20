from django.db import models

# Create your models here.
class ImageUpload(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    picture = models.ImageField(upload_to = 'myimage')
    date = models.DateTimeField(auto_now_add=True)


