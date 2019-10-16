from django.db import models

# Create your models here.

class Profile(models.Model):
    # user = 
    firstName = models.CharField(max_length = 30)
    lastName = models.CharField(max_length = 30)
    bio = models.CharField(max_length = 300)
    profile_pic = models.ImageField(upload_to = 'pictures/', null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
