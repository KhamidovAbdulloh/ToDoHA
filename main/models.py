from django.db import models


class Task(models.Model):
    title = models.CharField("Sarlavha", max_length=60)
    task = models.TextField('Yozishni boshlang')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'vazifa'
        verbose_name_plural = 'vazifalar'