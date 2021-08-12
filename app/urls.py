# -*- encoding: utf-8 -*-

#(username)stephen (password)stevolox

from django.urls import path, re_path
from app import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    path('diagnose/', views.diagnosis, name='diagnose'),
    path('result_list/', views.result_list, name='result_list'),
    path('exploratory_data_analysis/', views.eda, name = 'eda')

]