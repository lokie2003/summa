from django.db import models

class table1(models.Model):
    firstname=models.CharField(max_length=200)
    lastnmae=models.CharField(max_length=200)
    
