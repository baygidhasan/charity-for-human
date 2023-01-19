from django.db import models
# Create your models here.
class Charity(models.Model):
    doner_name=models.CharField(max_length=50)
    doner_address=models.CharField(max_length=100)
    doner_email=models.EmailField(max_length=30)
    doner_mob=models.IntegerField(max_length=15)

    class Meta:
        db_table="charity"
