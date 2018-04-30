from django.shortcuts import render, redirect
from django.contrib import messages
from models import *
import bcrypt
# Create your views here.
def index(request):
    return render(request, 'belt/index.html')

def register(request):
    errors = User.objects.register_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags = tag)
        return redirect('/')
    else:
        password = request.POST['password']
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        user = User.objects.create(
            name = request.POST['name'],
            alias = request.POST['alias'],
            email = request.POST['email'],
            password = hashed_password
        )
        messages.info(request, 'Successfully registered! Please login now')
        return redirect('/')
def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags = tag)
        return redirect('/')
    else:
        user = User.objects.get(email=request.POST['login_email'])
        request.session['id'] = user.id
        request.session['username'] = user.alias
        return redirect('/home_page')
def home(request):
    if 'id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['id'])
    reviews = Review.objects.all().order_by("-id")[:3]
    book = Book.objects.all()
    context = {
        'book': book,
        'review': reviews,
        'user': user
    }
    return render(request, 'belt/homepage.html', context)
def add_book(request):
    user = User.objects.get(id=request.session['id'])
    books = Book.objects.filter(user_book=user)
    context = {
        'book': books,
        'user': user
    }
    return render(request, 'belt/add_book_review.html')
def process_new_book(request):
    if 'id' not in request.session:
            return redirect('/')
    errors = Book.objects.new_book_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/add/book')
    else:
        author = request.POST['author_name']
        new_author = request.POST['new_author']
        current_user = User.objects.get(id=request.session['id'])
        if len(author) < 1:
            book = Book.objects.create(title=request.POST['title'], author=request.POST['new_author'], user_book=current_user)
            Review.objects.create(book_review=book, user_review=current_user, review=request.POST['review'], rating=request.POST['rating'])
            book_id = book.id
            return redirect('/show/book/details/'+ str(book_id))
        else:
            book = Book.objects.create(title=request.POST['title'], author=request.POST['author_name'], user_book=current_user)
            Review.objects.create(book_review=book, user_review=current_user, review=request.POST['review'], rating=request.POST['rating'])
            book_id = book.id
            return redirect('/show/book/details/'+ str(book_id))
def book_details(request, book_id):
    if 'id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['id'])
    book = Book.objects.filter(user_book=user)
    book_info = Book.objects.get(id=book_id)
    review = Review.objects.all()
    context = {
        'review': review,
        'book_info': book_info,
        
        'book': book,
        'user': user
    }
    return render(request, 'belt/book_details.html', context)
def destroy_reviews( request, book_id):
    pass
    # review = Review.objects.get(id=book_id)
    # review.delete()
    # return redirect('/show/book/details/' + str(book_id))
def add_review(request, book_id):
    user = User.objects.get(id=request.session['id'])
    book = Book.objects.get(user_book=user)
    review = Review.objects.create(
        review = request.POST['review'],
        rating = request.POST['rating'],
        book_review = book,
        user_review = user
    )
    return redirect('/show/book/details/' + str(book_id))
def user_details(request, user_id):
    pass
    # if 'id' not in request.session:
    #     return redirect('/')
    # context = {
    #     'user': User.objects.get(id=user_id),
    #     'all_user': Review.objects.all(),
    #     'totalRev': Review.objects.filter(id=user_id).count()
    # }
    # return render(request, 'belt/user_review.html', context)
def clear(request):
    if 'id' in request.session:
        request.session.clear()
    return redirect('/')
