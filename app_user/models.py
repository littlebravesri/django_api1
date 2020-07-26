from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=40, null=False)
    currentPassword = models.CharField(max_length=40, null=False)
    newPassword = models.CharField(max_length=40, null=False)

    def __str__(self):
        return str(self.name)
