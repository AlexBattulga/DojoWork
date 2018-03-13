#1 / - display "placeholder to later display all the list of blogs" via HttpResponse. Have this be handled by a method named 'index'.
#2 /new - display "placeholder to display a new form to create a new blog" via HttpResponse. Have this be handled by a method named 'new'.
#3 /create - Have this be handled by a method named 'create'.  For now, have this url redirect to /.
#4 /{{number}} - display 'placeholder to display blog {{number}}'.  For example /15 should display a message 'placeholder to display blog 15'.  Have this be handled by a method named 'show'.
#5 /{{number}}/edit - display 'placeholder to edit blog {{number}}.  Have this be handled by a method named 'edit'.
#6 /{{number}}/delete - Have this be handled by a method named 'destroy'. For now, have this url redirect to /.

from django.shortcuts import render, redirect, HttpResponse

def index(request):                                                             #1
    response = 'placeholder to later display all the list of blogs'
    return HttpResponse(response)
def new(request):                                                               #2
    response = 'placeholder to display a new form to create a new blog'
    return HttpResponse(response)
def create(request):                                                            #3
    return redirect('/')
def show(request, number):                                                      #4
    response = 'placeholder to display blog ', number
    return HttpResponse(response)
def edit(request, number):                                                      #5
    return HttpResponse('placeholder to edit blog ' + number)
def destroy(request, number):                                                   #6
    return redirect('/')
