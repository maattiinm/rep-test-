from django.db import models
from django.contrib.auth.models import User

class Expanse(models.Model):
    text = models.CharField( max_length = 255 )
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    def __unicode__(self) :
        return f"{self.date}-{self.amount}"

class Income(models.Model):
    text = models.CharField(max_length = 255 )
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    def __unicode__(self) :
        return f"{self.date}-{self.amount}"
