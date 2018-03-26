from django.shortcuts import render, redirect, HttpResponse
from models import *
from django.contrib import messages
import bcrypt
# Create your views here.
def index(request):
    return render(request, 'form/index.html', {'users': User.objects.all()})
def process(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        password = request.POST['rpassword']
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        user = User.objects.create()
        user.first_name = request.POST['fname']
        user.last_name = request.POST['lname']
        user.email = request.POST['email']
        user.password = hashed_password
        user.save()
        print user.password
        return redirect('/')
def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        user = User.objects.get(email = request.POST['email'])
        request.session['user'] = user.id
        return render(request, 'form/welcome.html', { 'users': User.objects.get(id=request.session['user'])})
