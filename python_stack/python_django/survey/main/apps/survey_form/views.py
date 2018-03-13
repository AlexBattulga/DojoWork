from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return render(request, 'blogs/index.html')
def process(request):
    if 'times' not in request.session:
        request.session['times'] = 0
    if request.method == 'POST':
        request.session['times'] += 1
        request.session['full_name'] = request.POST['full_name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
        if len(request.session['full_name']) < 1:
            return redirect('/')
        else:
            return redirect('/result')
    else:
        return redirect('/')
def result(request):
    return render(request, 'blogs/result.html')
def reset(request):
    request.session.clear()
    return redirect('/')
