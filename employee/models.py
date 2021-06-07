from django.db import models
from django.db.models import DO_NOTHING


# Create your models here.
from django.urls import reverse


class Department(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return "Department of " + self.name


class Employee(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    cnic = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='employee/', null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=DO_NOTHING, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')
