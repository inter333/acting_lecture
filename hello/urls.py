from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'sampleapp'

urlpatterns =[
        path('', views.MonthCalendar.as_view(), name='month'),
        path('index', views.index,name='index'),
        path('create',views.create,name='create'),
        path('month/<int:year>/<int:month>', views.MonthCalendar.as_view(), name='month'),
]
