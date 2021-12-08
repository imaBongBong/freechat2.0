from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
import uuid
from user.models import Profile

# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now=True)
    edited = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created']
    def __str__(self):
        return self.name

class Room(models.Model):
    name = models.CharField(max_length=200)
    #messages
    topic = ForeignKey(Topic,on_delete=CASCADE,null=True,blank=True)
    owner = ForeignKey(Profile,on_delete=CASCADE,null=True,blank=True)
    created = models.DateTimeField(auto_now=True)
    edited = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True,blank=True)
    participants = models.ManyToManyField(Profile,related_name='participants',blank=True)
    

    class Meta:
        ordering = ['-created']
    
    def __str__(self):
        return self.name

    
        

class UserMessage(models.Model):
    owner = models.ForeignKey(Profile,on_delete=CASCADE,null=True,blank=True)
    room = models.ForeignKey(Room,on_delete=CASCADE,null=True,blank=True)
    body = models.TextField()
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    created = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-created']
    def __str__(self):
        return self.body[:50]
