from django.db import models


class RandomNumber(models.Model):
    number = models.IntegerField(blank=False)

    def __str__(self):
        return str(self.number)

    class Meta:
        verbose_name = 'Generated number'
