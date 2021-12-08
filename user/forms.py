from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from user.models import Profile

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','email','username','password1','password2']
        labels = {'first_name':'Name',}
    

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name','email','profile_image','short_intro','long_intro']

    def __init__(self,*args,**kwargs):
        super(ProfileForm,self).__init__(*args,**kwargs)

        for k,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})