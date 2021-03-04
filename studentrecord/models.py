from django.db import models

# Create your models here.

class Studentrecord(models.Model):
    Id = models.AutoField(primary_key=True)
    RollNo = models.IntegerField()
    Name = models.CharField(max_length=60)
    Maths = models.IntegerField()
    Physics = models.IntegerField()
    Chemistry = models.IntegerField()
    Total = models.IntegerField()
    Percentage = models.FloatField()
    
    def __str__(self):
        return self.Name