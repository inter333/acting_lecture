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
from . forms import SearchForm
from .models import Schedule




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
    if (request.method == 'POST'):
        date = request.POST['date']
        time = request.POST['time']
        name = request.POST['name']
        grade = request.POST['grade']
        subject = request.POST['subject']
        remark = request.POST['remark']
        print(request.user.username)
        classes = Classes(date=date,time=time,name=name,\
                grade=grade,subject=subject,remark=remark,act_user=request.user.username)
        classes.save()
        year = str(year)
        month = str(month)
        day = str(day)
        return redirect(to='/hello/index/'+year+'/'+month+'/'+day)
    return render(request,'hello/index.html',params)

@login_required(login_url='/hello/login/')
def register(request,num,year,month,day):
    classes = Classes.objects.get(id=num)
    classes.act_user = request.user.username
    classes.save()
    year = str(year)
    month = str(month)
    day = str(day)
    return redirect(to='/hello/index/'+year+'/'+month+'/'+day)

@login_required(login_url='/hello/login/')
def cancel(request,num,year,month,day):
    classes = Classes.objects.get(id=num)
    classes.act_user = ""
    classes.save()
    year = str(year)
    month = str(month)
    day = str(day)
    return redirect(to='/hello/index/'+year+'/'+month+'/'+day)




@login_required(login_url='/hello/login/')
def create(request,year,month,day):
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
    data = Classes.objects.filter()

    classform = ClassesForm()
    classform.fields["date"] = forms.DateField(initial=str(year) + '-' + str(month) + '-' + str(day))

    params = {
        'title':'代行要請',
        'message':'top',
        'msg':'前に戻る',
        'form':classform,
        'data':data,
        'year':year,
        'month':month,
        'day':day,
    }
    print(classform)
    
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
    params = {
        'title': '代行要請',
        'messege':'top',
        'msg':'前に戻る',
        'form':ClassesForm(instance=data),
        'id':num,
        'year':year,
        'month':month,
        'day':day,
    }
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
        'messege':'top',
        'msg':'前に戻る',
        'id':num,
        'data':classes,
        'year':year,
        'month':month,
        'day':day,
    }
    return render(request,'hello/delete.html',params)

@login_required(login_url='/hello/login/')
def search(request):
    if (request.method == 'POST'):
        msg = '調べたい日付をYYYY-MM-DD形式で検索してください。'
        form = SearchForm(request.POST)
        str = request.POST['search']
        data = Classes.objects.filter(date=str)
    else:
        msg = '調べたい日付をYYYY-MM-DD形式で検索してください。'
        form = SearchForm()
        data = Classes.objects.all()
    params = {
        'title':'代行要請日の検索',
        'message':msg,
        'form':form,
        'data':data,
    }
    return render(request,'hello/search.html',params)






class MonthCalendar(LoginRequiredMixin,mixins.MonthCalendarMixin, generic.TemplateView):
    login_url = '/login/'
    """月間カレンダーを表示するビュー"""
    template_name = 'hello/month.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_month_calendar()
        context.update(calendar_context)
        return context


class MonthWithScheduleCalendar(mixins.MonthWithScheduleMixin, generic.TemplateView):
    login_url = '/login/'
    """スケジュール付きの月間カレンダーを表示するビュー"""
    template_name = 'hello/month_with_schedule.html'
    model = Classes
    date_field = 'date'
    data = Classes.objects.all()

    def get_context_data(self,year,month,**kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_month_calendar()
        context.update(calendar_context)
        context['data'] = Classes.objects.filter(date__year=year,date__month=month)
        return context

