from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
from models import *
from django.contrib import messages
import bcrypt
# Create your views here.
def index(request):
    return render(request, 'dash/index.html')
def signin(request):
    return render(request, 'dash/signin.html')
# Sign in process page!!!
def process_signin(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/signin')
    else:
        return redirect('/display_dash')
def display_dash(request):
    return render(request, 'dash/dashboard.html', {'users': User.objects.all()})
def register(request):
    return render(request, 'dash/register.html')
# Register in process page!!!
def process_register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/register')
    else:
        user_password = request.POST['password']
        hashed_password = bcrypt.hashpw(user_password.encode(), bcrypt.gensalt())
        User.objects.create(
            first_name = request.POST['fname'],
            last_name = request.POST['lname'],
            email = request.POST['email'],
            password = hashed_password
        )
        return redirect('/signin')
# Create new Users
def create(request):
    return render(request, 'dash/create_user.html')
# Create page process
def process_create(request):
    errors_data = User.objects.basic_validator(request.POST)
    if len(errors_data):
        for tag, error in errors_data.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/create')
    else:
        userPassword = request.POST['password']
        hashed_password = bcrypt.hashpw(userPassword.encode(), bcrypt.gensalt())
        User.objects.create(
            first_name = request.POST['fname'],
            last_name = request.POST['lname'],
            email = request.POST['email'],
            password = hashed_password
        )
        return redirect('/display_dash')
# User edit
def edit(request, id):
    return render(request, 'dash/edit_user.html', {'users': User.objects.get(id=id)})
# Edit page process
def process_edit(request, id):
    errors = User.objects.edit_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/edit/'+id)
    else:
        user = User.objects.get(id=id)
        user.email = request.POST['email']
        user.first_name = request.POST['fname']
        user.last_name = request.POST['lname']
        user.save()
        return redirect('/display_dash')
# Updating user's password
def process_password(request, id):
    errors = User.objects.password_update_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/edit/'+id)
    else:
        user_password = request.POST['password']
        hashed_password = bcrypt.hashpw(user_password.encode(), bcrypt.gensalt())
        user = User.objects.get(id=id)
        user.password = hashed_password
        user.save()
        return redirect('/display_dash')
# Delete user
def destroy(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('/display_dash')
# Navigator to profile page
def profile(request, id):
    return render(request, 'dash/profile.html', {'users': User.objects.filter(id=id)})
# Processing a messages
def process_message(request, id):
    user = User.objects.all()
    user_message = Message.objects.create(message = request.POST['message'], user = user)
    return redirect('/profile/'+id)
