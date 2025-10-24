from django.db import models

class Cat(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    clicks = models.IntegerField(default=0)
    milk = models.IntegerField(default=0)
    level = models.IntegerField(default=1)

    def __str__(self):
        return self.name

    def level_up(self):
        if self.clicks >= 10 * self.level:
            self.level += 1
            self.milk += 5
            self.save()

