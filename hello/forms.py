from django import forms

class HelloForm(forms.Form):
    date = forms.DateField(label='date')
    time = forms.TimeField(label='time')
    name = forms.CharField(label='name')
    grade = forms.CharField(label='grade')
    subject = forms.CharField(label='subject')
    remark = forms.CharField(label='remark')

