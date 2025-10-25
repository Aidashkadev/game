from django.db import models

class Cat(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    score = models.IntegerField(default=0)   # formerly clicks
    milk = models.IntegerField(default=0)
    level = models.IntegerField(default=1)

    def __str__(self):
        return self.name

    def level_up(self):
        # example: level up every 10 * current level points
        if self.score >= 10 * self.level:
            self.level += 1
            self.milk += 5
            self.save()
class Cat(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='cats/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    mood = models.CharField(max_length=20, choices=[('happy','Счастливый'),('grumpy','Сердитый'),('sleepy','Сонный')], default='happy')
    milk = models.IntegerField(default=0)
    score = models.IntegerField(default=0)  # ← вот это добавляем
