from django.shortcuts import render

# Create your views here.
from .calendar_API import test_calendar

def demo(request):
    results = test_calendar()
    context = {"results": results}
    return render(request, 'demo.html', context)

def home(request):
    return render(request, 'home.html')

# def project(request):
#     return render(request, 'project.html')
