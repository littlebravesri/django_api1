from django.db import models


class ItemList(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.IntegerField(default=0)
    type = models.IntegerField(default=0)
    name = models.TextField(max_length=40, null=False)
    city = models.TextField(max_length=40, null=False)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'ItemList'
        verbose_name_plural = 'ItemLists'
