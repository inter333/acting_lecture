from django import forms
from.models import Users,Classes,Act_person

class ClassesForm(forms.Form):
    date    = forms.DateField(label='date')
    time    = forms.TimeField(label='time')
    name    = forms.CharField(label='name')
    grade   = forms.CharField(label='grade')
    subject = forms.CharField(label='subject')
    remark  = forms.CharField(label='remark',required=False)
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



