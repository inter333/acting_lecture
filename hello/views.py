from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import redirect
from .forms import ClassesForm
from .models import Classes


def calender(request):
    return render(request,'hello/calender.html')

class HelloView(TemplateView):

    def __init__(self):
        self.params = {
               'title':'代行要請',
               'message':'コマの情報',
               'form':ClassesForm()
            }
    
    def get(self,request):
        return render(request,'hello/index.html',self.params)


    def post(self,request):
        cls = Classes()
        cls.date = request.POST['date']
        cls.time = request.POST['time']
        cls.subject = request.POST['subject']
        print(str(request.POST['subject']))


        self.params['form'] = ClassesForm(request.POST)
        self.params['form'] = ClassesForm(request.POST)
        return render(request,'hello/index.html',self.params)


def index(request):
    data = Classes.object.all()
    params = {
        'title':'Hello',
        'data':data,
        }
    return render(request,'hello/index.html',params)

#create model
def create(request):
    params = {
        'title':'Hello',
        'form':ClassesForm(),
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
        return redirect(to='/hello/calender')
    return render(request,'hello/create.html',params)



