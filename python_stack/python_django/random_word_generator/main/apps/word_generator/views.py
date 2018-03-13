from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):                                                             # counter session is an equal to 1
    if 'counter' not in request.session:
        request.session['counter'] = 1
    if request.method == 'POST':                                                # counter session will increment by 1 everytime form submited
        request.session['counter'] += 1
    random_string = {                                                           # generating a random string using get_random_string and length of 14
        'number': get_random_string(length=14)
    }
    return render(request, 'blogs/index.html', random_string)                   # passing a dict to index
def reset(request):                                                             # resets an attempt
    request.session.clear()
    return redirect('/')
