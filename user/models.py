from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models.deletion import CASCADE

from django.db.models.fields.related import OneToOneField
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=CASCADE,null=True,blank=True)
    name = models.CharField(max_length=200,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    profile_image = models.ImageField(null=True,blank=True,upload_to='profile/',default='profile/default.png')
    short_intro = models.TextField(null=True,blank=True)
    long_intro = models.TextField(null=True,blank=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    
    @property
    def image_url(self):
        try:
            url = self.profile_image.url
        except:
            url = '/images/profile/default.png'
            
        return url