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



def index(request, year, month, day):
    data = Classes.objects.filter(date__year=year,date__month=month,date__day=day)
    params = {
             'title':'代行情報',
             'message':'代行要請',
             'msg':'top',
             'form':'Classesform',
             'data':data,
    }
    return render(request,'hello/index.html',params)

#create model
def create(request):
    data = Classes.objects.filter()
    params = {
        'title':'代行要請',
        'message':'top',
        'form':ClassesForm(),
        'data':data
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



class MonthCalendar(LoginRequiredMixin,mixins.MonthCalendarMixin, generic.TemplateView):
    login_url = '/login/'
    """月間カレンダーを表示するビュー"""
    template_name = 'hello/month.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_month_calendar()
        context.update(calendar_context)
        return context



