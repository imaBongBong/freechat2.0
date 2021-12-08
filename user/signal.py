from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from .models import Profile
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings


def create_profile(sender,instance,created,**kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            name = user.first_name,
            email = user.email,
        )

post_save.connect(create_profile,sender = User)