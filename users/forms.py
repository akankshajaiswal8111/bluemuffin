from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from .models import Files
from .sizeChecker import SizeRestrictedFileField

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields

#class DocumentForm(forms.ModelForm):
    
#    class Meta:
#        model = Files
#        fields = ('description', 'file',)
class DocumentForm(forms.ModelForm):
    class Meta:
        model = Files
        fields = ('description', 'file')
        file = SizeRestrictedFileField()

