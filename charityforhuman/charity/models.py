from django.db import models
# Create your models here.
class Charity(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    email=models.EmailField(max_length=30)
    mob=models.IntegerField(max_length=15)

    class Meta:
        db_table="charitys"
