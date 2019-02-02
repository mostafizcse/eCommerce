from django.db import models

# Create your models here.

class CustomarRegistration(models.Model):
    name = models.CharField(max_length=20)
    username = models.CharField(max_length=25)
    email = models.EmailField()
    password_1 = models.CharField(max_length=30, verbose_name='Password')
    password_2 = models.CharField(max_length=30, verbose_name='Password 2')

    def __str__(self):
        return self.username
