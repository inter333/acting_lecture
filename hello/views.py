from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import redirect
from .forms import ClassesForm
from .models import Classes
from django.views import generic
from . import mixins





def index(request):
    data = Classes.objects.all()
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
    data = Classes.objects.all()
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
        return redirect(to='/hello/index')
    return render(request,'hello/create.html',params)

class MonthCalendar(mixins.MonthCalendarMixin, generic.TemplateView):
    """月間カレンダーを表示するビュー"""
    template_name = 'hello/month.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_month_calendar()
        context.update(calendar_context)
        return context



