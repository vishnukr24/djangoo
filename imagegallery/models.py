from django.db import models

class ImageGallery(models.Model):
    caption = models.CharField(max_length=100)
    image = models.ImageField(upload_to="img")

    def __str__(self):
        return self.caption
    
