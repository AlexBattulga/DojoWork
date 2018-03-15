from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
def index(request):
    if 'word' not in request.session:
        request.session['word'] = []
    return render(request, 'blogs/index.html')
def process(request):
    date = strftime('%r:%M:%S %p %b %d, %Y')
    try:
        word = request.POST['word']
        color = request.POST['color']
    except:
        return redirect('/')
    if 'big_font' in request.POST:
        big_font = request.POST['big_font']
    else:
        big_font=False
    if request.method == 'POST':
        if 'word' in request.session:
            words = request.session['word']
            words.append({
                'word': word,
                'color': color,
                'date': date,
                'big_font': big_font
            })
            request.session['word'] = words
            return redirect('/')
    else:
        return redirect('/')
def result(request):
    return redirect('/')
def clear(request):
    request.session.clear()
    return redirect('/')
