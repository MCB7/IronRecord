from django.db import models
from  django.contrib.auth.models import User

# Create your models here.
# Each model will become a table in the database
class ExcerciseDate(models.Model):
    excercisedate=models.CharField(max_length=255)
    excercisetype=models.CharField(max_length=255)
    def __str__(self):
        return self.excercisedate
    
    class Meta:
        db_table='excercisedate'
    
class ExcerciseDetail(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    excerciseedate=models.ForeignKey(ExcerciseDate, on_delete=models.CASCADE)
    liftname=models.CharField(max_length=255)
    lift1setweight=models.SmallIntegerField()
    lift1repnumber=models.SmallIntegerField()
    lift2setweight=models.SmallIntegerField()
    lift2repnumber=models.SmallIntegerField()
    lift3setweight=models.SmallIntegerField()
    liftrepnumber=models.SmallIntegerField()
    liftnote=models.CharField(max_length=255)
    
    def __str__(self):
        return self.liftname
    
    class Meta:
        db_table='excercisedetail'
