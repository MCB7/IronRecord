from django.shortcuts import render, get_object_or_404
from .models import ExcerciseDate, ExcerciseDetail
from django.urls import reverse_lazy
from .forms import ExerciseForm

# Create your views here.
def index(request):
    return render(request, 'ir0n/index.html')

def excercisedetail(request):
    excercisedetail_list=ExcerciseDetail.objects.all()
    return render(request, 'ir0n/excercisedetail.html', {'excercisedetail_list': excercisedetail_list})

def excerciseinfo(request, id):
    detail=get_object_or_404(ExcerciseDetail, pk=id)
    return render(request, 'ir0n/excerciseinfo.html', {'detail' : detail})

def newExercise(request):
    form=ExerciseForm

    if request.method=='POST':
        form=ExerciseForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ExerciseForm()
    else:
        form=ExerciseForm()
    return render(request, 'ir0n/newexercise.html', {'form': form})