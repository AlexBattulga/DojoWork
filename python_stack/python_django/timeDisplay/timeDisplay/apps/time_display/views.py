from django.shortcuts import render, redirect, HttpResponse
from time import gmtime, strftime
def index(request):
    context = {
        'time': strftime('%b %d, %Y %H:%M%p', gmtime())
    }
    return render(request, 'blogs/index.html', context)
