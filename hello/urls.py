from django.conf.urls import url
from .views import HelloView
from django.urls import path
from . import views


urlpatterns =[
        path('', HelloView.as_view(),name='index'),
        path('calender',views.calender,name='calender'),
        path('create',views.create,name='create')
]
