from django.db import models

# Create your models here.
"""
'Type' model take in the correlation required

'Dataset' model is to read the csv file into the database and 
perform the necessary CRUD and coreelation calculation operation

"""

class Type(models.Model):
    correlation = models.CharField(max_length=40, null=False)

    def __str__(self):
        return str(self.name)


class Dataset(models.Model):
    date_w = models.TextField(max_length=40, null=False)
    price = models.FloatField(max_length=40, null=False)
    total_vol = models.FloatField(max_length=40, null=False)
    plu1 = models.FloatField(max_length=40, null=False)
    plu2 = models.FloatField(max_length=40, null=False)
    plu3 = models.FloatField(max_length=40, null=False)
    bags_t = models.FloatField(max_length=40, null=False)
    bags_s = models.FloatField(max_length=40, null=False)
    bags_l = models.FloatField(max_length=40, null=False)
    bags_lx = models.FloatField(max_length=40, null=False)
    type = models.TextField(max_length=40, null=False)
    year = models.TextField(max_length=40, null=False)
    location = models.TextField(max_length=40, null=False)

    def __str__(self):
        return str(self.name)