from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import redirect
from .forms import ClassesForm
from .models import Classes
from django.views import generic
from . import mixins
from .forms import SignUpForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django import forms



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(to='/hello/')
    else:
        form = SignUpForm()
    return render(request, 'hello/signup.html', {'form': form})


@login_required(login_url='/hello/login/')
def index(request, year, month, day):
    data = Classes.objects.filter(date__year=year,date__month=month,date__day=day)
    #user_id = request.user.id
    params = {
             'title':'代行情報',
             'message':'代行要請',
             'msg':'top',
             'form':'Classesform',
             'data':data,
             'year':year,
             'month':month,
             'day':day,
             #'user_id':user_id
    }
    return render(request,'hello/index.html',params)

@login_required(login_url='/hello/login/')
def create(request,year,month,day):
    data = Classes.objects.filter()
    params = {
        'title':'代行要請',
        'message':'top',
        'form':ClassesForm(),
        'data':data,
        'year':year,
        'month':month,
        'day':day,

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
        year = str(year)
        month = str(month)
        day = str(day)
        return redirect(to='/hello/index/'+year+'/'+month+'/'+day)
    return render(request,'hello/create.html',params)

@login_required(login_url='/hello/login/')
def edit(request,num,year,month,day):
    data = Classes.objects.get(id=num)
    if (request.method == 'POST'):
        classes = ClassesForm(request.POST,instance=data)
        #classes.act_user = request.user.username
        classes.save()
        year = str(year)
        month = str(month)
        day = str(day)
        return redirect(to='/hello/index/'+year+'/'+month+'/'+day)

    form = ClassesForm(instance=data)
    form.fields['act_user'].widget = forms.CharField(label='act_user',required=False)     
    params = {
        'title': '代行要請',
        'form':ClassesForm(instance=data),
        'id':num,
        'year':year,
        'month':month,
        'day':day,
    }
    print(request.user.username)
    return render(request,'hello/edit.html',params)

@login_required(login_url='/hello/login/')
def delete(request,num,year,month,day):
    classes = Classes.objects.get(id=num)
    if (request.method == 'POST'):
        classes.delete()
        year = str(year)
        month = str(month)
        day = str(day)
        return redirect(to='/hello/index/'+year+'/'+month+'/'+day)
    params = {
        'title':'代行要請削除',
        'id':num,
        'data':classes,
        'year':year,
        'month':month,
        'day':day,
    }
    return render(request,'hello/delete.html',params)






class MonthCalendar(LoginRequiredMixin,mixins.MonthCalendarMixin, generic.TemplateView):
    login_url = '/login/'
    """月間カレンダーを表示するビュー"""
    template_name = 'hello/month.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_month_calendar()
        context.update(calendar_context)
        return context



