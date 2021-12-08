from django.contrib import admin
from .models import Room,Topic,UserMessage
# Register your models here.
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(UserMessage)