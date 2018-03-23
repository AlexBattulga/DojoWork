from django.shortcuts import render, HttpResponse, redirect
from models import *
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'course/index.html', {'name': Name.objects.all()})
def decision(request, id):
    request.session['id'] = id
    return render(request, 'course/destroy.html', {'name': Name.objects.get(id=id)})
def destroy(request, id):
    destroy_course = Name.objects.get(id = id)
    destroy_course.delete()
    return redirect('/')
def add(request):
    errors = Name.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.items():
            messages.error(request, error, extra_tags = tag)
        return redirect('/')
    else:
        if request.method == 'POST':
            d = Desc.objects.create(course_desc=request.POST['desc'])
            c = Name.objects.create(course_name=request.POST['name'], desc=d)
        return redirect('/')
