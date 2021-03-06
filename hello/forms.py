from django import forms
from .models import Users,Classes,Act_person
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

class ClassesForm(forms.ModelForm):
    class Meta:
        model  = Classes
        fields = ['date','time','name','grade','subject','remark']
        widgets = {'act_user':forms.HiddenInput(),
            }

##バリデーション



class UsersForm(forms.Form):
    name     = forms.CharField(label='name')
    mail     = forms.EmailField(label='mail')
    passward = forms.CharField(label='passward')

class Act_personForm(forms.Form):
    act_person_name = forms.CharField(label='act_person_name')
    date            = forms.DateField(label='date')
    time            = forms.TimeField(label='time')

class PostForm(forms.Form):
    subject         = forms.CharField(max_length=100,widget=forms.Textarea)
    class Meta:
        model  = Classes
        fields = ['subject']

class SearchForm(forms.Form):
    search = forms.CharField(label='Search',required=False)



