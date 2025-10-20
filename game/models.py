from django.db import models

class Cat(models.Model):
    name = models.CharField(max_length=50)
    milk = models.IntegerField(default=0)
    level = models.IntegerField(default=1)
    mood = models.CharField(max_length=20, default='happy')

    def __str__(self):
        return f"{self.name} (Lvl {self.level})"
