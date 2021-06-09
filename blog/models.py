from django.db import models
from datetime import date

class post(models.Model):
    title=models.CharField(max_length=200)
    body=models.TextField()
    date=models.DateField(null=True,default=date.today)
    

class Comment(models.Model):
    post = models.ForeignKey(post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    body = models.TextField()
    date_added =models.DateField(null=True,default=date.today)
    
 
class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    


# Create your models here.
