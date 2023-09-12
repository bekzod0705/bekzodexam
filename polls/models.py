from django.db import models
from datetime import datetime

# Create your models here.

class authorModel(models.Model):
    name=models.CharField(max_length=60,default='')
    lastname=models.CharField(max_length=60,default='')
    birthday=models.DateTimeField()
    ismarried=models.BooleanField(default=False)
    class Meta:
        db_table='author'
    def __str__(self) -> str:
        return self.name
        


class bookModel(models.Model):
    name=models.CharField(max_length=60,default='')
    page=models.IntegerField(default=0)
    desc=models.TextField(default='write!')
    created_at=models.DateTimeField(default=datetime.now)
    author=models.ForeignKey(authorModel,on_delete=models.CASCADE)
    class Meta:
        db_table='book'
    def __str__(self) -> str:
        return self.name
    

