from django.contrib import admin
from django.urls import path, include
from .views import home, exam, result

urlpatterns = [
    path('', home, name ='home'),
    path('exam/', exam, name= 'exam'),
    path('result/', result, name= 'result'),
] 