from django.db import models

# Create your models here.
class Detail(models.Model):
    positive_no = models.CharField(max_length=200, null=True, blank=True)
    invalid_no = models.CharField(max_length=200, null=True, blank=True)
    min_no = models.CharField(max_length=200, null=True, blank=True)
    max_no = models.IntegerField(max_length=200, null=True, blank=True)
    avg = models.IntegerField(null=True, blank=True)


class Booking(models.Model):
    no_of_slot = models.IntegerField()
    name1 = models.CharField(max_length=200)
    name2 = models.CharField(max_length=200,null=True, blank=True)
    status = models.BooleanField(default=False)