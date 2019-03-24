from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns =[
        path('', views.index,name='index'),
        path('calender',views.calender,name='calender'),
        path('create',views.create,name='create'),
]
