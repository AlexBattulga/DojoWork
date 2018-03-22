from django.shortcuts import render, HttpResponse, redirect
from models import*
from django.contrib import messages
from datetime import datetime

# Create your views here.
def index(request):
    myDate = datetime.now()
    formatedDate = myDate.strftime('%Y-%m-%d')
    return render(request, 'resftul/index.html', {'users': User.objects.all() }, {'date': formatedDate})
def show(request, id):
    return render(request, 'resftul/show.html', {'users_info': User.objects.get(id=id)})
def edit(request, id):
    return render(request, 'resftul/edit.html', {'users_info': User.objects.get(id=id)})
def update(request, id):
    if request.method == 'POST':
        user = User.objects.get(id = id )
        user.first_name = request.POST['f_name']
        user.last_name = request.POST['l_name']
        user.email = request.POST['email']
        user.save()
        return redirect('/users/update/'+ id)
    else:
        return redirect('/')
def destroy(request, id):
    user = User.objects.get(id = id )
    user.delete()
    return redirect('/')
def new(request):
    return render(request, 'resftul/new.html')
def create(request):

    User.objects.create(first_name = request.POST['fname'], last_name = request.POST['lname'], email = request.POST['email_add'])
    return redirect('/')
