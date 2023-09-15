from django.db import models

class forum(models.Model):
    name = models.CharField(max_length=200, default="anonymous")
    email = models.EmailField(max_length=200, null=True)
    topic = models.CharField(max_length=300)
    description = models.CharField(max_length=1000, blank=True)
    link = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    
