from django.db import models


# Create your models here.
class HRManager(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    cnic = models.PositiveBigIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name