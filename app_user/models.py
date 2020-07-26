from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=40, null=False)
    password = models.CharField(max_length=40, null=False)
    confirmpassword = models.CharField(max_length=40, null=False, required = True)

    def __str__(self):
        return str(self.name)
