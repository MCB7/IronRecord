from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('excercisedetails/', views.excercisedetail, name='excercisedetail'),
    path('excerciseinfo/<int:id>', views.excerciseinfo, name='info'),
]
