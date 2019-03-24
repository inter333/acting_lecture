from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import redirect
from .forms import ClassesForm
from .models import Classes


def calender(request):
    return render(request,'hello/calender.html')


def index(request):
    data = Classes.objects.all()
    params = {
             'title':'Hello',
             'message':'all classes',
             'form':'Classesform',
             'data':data,
    }
    return render(request,'hello/index.html',params)

#create model
def create(request):
    data = Classes.objects.all()
    params = {
        'title':'Hello',
        'data':data,
    }
    if (request.method == 'POST'):
        date = request.POST['date']
        time = request.POST['time']
        name = request.POST['name']
        grade = request.POST['grade']
        subject = request.POST['subject']
        remark = request.POST['remark']
        classes = Classes(date=date,time=time,name=name,\
                 grade=grade,subject=subject,remark=remark)
        classes.save()
        return redirect(to='/hello/')
    return render(request,'hello/create.html',params)



