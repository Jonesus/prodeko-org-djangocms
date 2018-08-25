from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Course

def index(request):
    courses = Course.objects.all()
    return render(request, 'lifelonglearning.html', {
        'courses': courses,
    })

def coursepage(request, pk):
    course = Course.objects.get(pk = pk)
    return render(request, 'coursepage.html', {
        'course': course,
    })