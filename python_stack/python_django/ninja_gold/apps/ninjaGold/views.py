from django.shortcuts import render, redirect, HttpResponse
import random, datetime

def index(request):
    if 'myGold' not in request.session:
        request.session['myGold'] = 0
        request.session['message'] = []

    return render(request, 'ninjaGold/index.html')
def process(request, name):
    print name
    now = datetime.datetime.now()
    today = now.strftime('%Y-%m-%d %I:%M %p')
    if request.method == 'POST':
        if name == 'farm':
            goldEarned = random.randrange(10, 21)
            print goldEarned
            detail = ('Earned {} golds from Farm! ({})'.format(goldEarned, today))
            request.session['message'].insert(0, detail)
            print request.session['message']
        elif name == 'cave':
            goldEarned = random.randrange(5, 10)
            print goldEarned
            detail = ('Earned {} golds from Cave! ({})'.format(goldEarned, today))
            request.session['message'].insert(0, detail)
            print request.session['message']
        elif name == 'house':
            goldEarned = random.randrange(2, 5)
            print goldEarned
            detail = ('Earned {} golds from house! ({})'.format(goldEarned, today))
            request.session['message'].insert(0, detail)
            print request.session['message']
        else:
            goldEarned = random.randrange(-50, 51)
            print goldEarned
            if goldEarned >=0:
                message = 'Yay! You earned {} gold from the casino! ({})'.format(goldEarned, today)
            else:
                message = 'Entered a casino and lost {} golds...Ouch...({})'.format(goldEarned, today)

            request.session['message'].insert(0, message)
    request.session['myGold'] += goldEarned;
    return redirect('/')
def clear(request):
    request.session.clear()
    return redirect('/')
