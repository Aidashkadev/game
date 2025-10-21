from django.db import models

class Cat(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image_url = models.URLField(blank=True)

    def __str__(self):
        return self.name
