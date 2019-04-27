from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django .views.generic import TemplateView



app_name = 'sampleapp'

urlpatterns = [
        path('login/', LoginView.as_view(template_name = 'hello/login.html'), name="login"),
        path('logout/',LogoutView.as_view(template_name = 'hello/logout.html'), name="logout"),
        path('', views.MonthCalendar.as_view(), name='month'),
        path('index', views.index,name='index'),
        path('index/<int:year>/<int:month>/<int:day>', views.index, name='index'),
        path('create/<int:year>/<int:month>/<int:day>',views.create,name='create'),
        path('month/<int:year>/<int:month>', views.MonthCalendar.as_view(), name='month'),
        path ('signup',views.signup,name='signup'),
        path('edit/<int:num>/<int:year>/<int:month>/<int:day>',views.edit,name='edit'),
        path('delete/<int:num>/<int:year>/<int:month>/<int:day>',views.delete,name='delete'),
        path('search',views.search,name='search'),
        path('register/<int:num>/<int:year>/<int:month>/<int:day>',views.register,name='register')
]