# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 00:00:25 2019

@author: namek
"""

from django.conf.urls import url
from . views import HelloView

urlpatterns = [
        url(r'',HelloView.as_view(),name='index'),
]