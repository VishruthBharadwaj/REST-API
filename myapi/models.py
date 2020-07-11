from django.db import models
from django.utils.timezone import datetime
from datetime import datetime
import time



class Member(models.Model):
    name = models.CharField(max_length=60)
    id_no= models.CharField(max_length=60)
    tz= models.CharField(max_length=60)
    time=time.strftime("%H:%M:%S")
    date=models.DateField(default='%d %b, %Y')
     

   
    def __str__(self):
        return self.name