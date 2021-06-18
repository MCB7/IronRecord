from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('excercisedetails/', views.excercisedetail, name='excercisedetail'),
    path('excerciseinfo/<int:id>', views.excerciseinfo, name='info'),
    path('newexercise/', views.newExercise, name="newexercise"),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]
