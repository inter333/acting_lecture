from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import HelloForm

class HelloView(TemplateView):

    def __init__(self):
        self.params = {
               'title':'代行要請',
               'message':'コマの情報',
               'form':HelloForm()
            }
    
    def get(self,request):
        return render(request,'hello/index.html',self.params)


    def post(self,request):
        msg = '入力した情報は以下の通りですか？<br><b>'  '(' + request.POST['date'] + \
            ')' '(' + request.POST['time'] + \
            ')</b><b>' + request.POST['name'] + \
            '(' + request.POST['grade'] + \
            ')' + request.POST['subject'] + \
            '(' + request.POST['remark'] + \
            ')' '</b>'
        self.params['message'] = msg
        self.params['form'] = HelloForm(request.POST)
        self.params['message'] = msg
        self.params['form'] = HelloForm(request.POST)
        return render(request,'hello/index.html',self.params)



