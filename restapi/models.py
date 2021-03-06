from django.db import models

# Create your models here.
class Bank(models.Model):
    name = models.CharField(max_length=49, null=True)
    id = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'banks'


class Branch(models.Model):
    ifsc = models.CharField(max_length=11, primary_key=True)
    bank = models.ForeignKey(Bank, on_delete=models.PROTECT, null=True)
    branch = models.CharField(max_length=74, null=True)
    address = models.CharField(max_length=195, null=True)
    city = models.CharField(max_length=50, null=True)
    district = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)

    class Meta:
        managed = False
        db_table = 'branches'
