# main/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser



# main/models.py



class customuser(AbstractUser):
    age = models.PositiveBigIntegerField(default=21)
    profile_pic = models.FileField(upload_to='profile_pics/', blank=True, null=True)



#notifications

from django.conf import settings

class Notification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.user.username} - {self.message}" 
    
    
    
    
    
class Person(models.Model):
    name = models.CharField(max_length=200)
    age=models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='course_images/', null=True, blank=True)
    #image = models.ImageField(upload_to='course_images/', null=True, blank=True)  # Optional course image

    def __str__(self):
        return self.title


    
 
 
