from django.contrib import admin
from .models import ImageUpload

# Register your models here.
@admin.register(ImageUpload)
class ImageUploadAdmin(admin.ModelAdmin):
    # Ordering fields name
    list_display = ['id', 'title', 'desc', 'picture', 'date']



