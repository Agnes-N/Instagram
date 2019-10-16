from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User

# Create your models here.

class Image(models.Model):
    '''
    a class for Image model
    '''
    image_caption = models.CharField(max_length =30)
    image_name = models.CharField(max_length =30,null=True)
    profile_pic = models.ImageField(upload_to = 'profile_pics/', null=True)
    date = models.DateTimeField(auto_now_add=True)

    @classmethod
    def get_all_images(cls):
        images = cls.objects.all()
        return images

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_image(cls,id,value):
        cls.objects.filter(id = id).update(profile_pic = new_profile_pic)

    def __str__(self):
        return self.image_caption

class Profile(models.Model):
    firstname = models.CharField(max_length =30)
    lastname = models.CharField(max_length =30)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to = 'profile_photos/', null=True)
    bio = HTMLField()
    date = models.DateTimeField(auto_now_add=True)

    @classmethod
    def get_all_users(cls):
        instagram_users = cls.objects.all()
        return instagram_users

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def update_profile(cls,id,value):
        cls.objects.filter(id = id).update(user_id = new_user)


def __str__(self):
        return self.user