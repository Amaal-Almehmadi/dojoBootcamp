from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt
from datetime import date

def index(request):
    if 'uid' in request.session:
        return redirect("/wishes")
    context = {
        'today': date.today()
    }
    return render(request, "home.html", context)

def wishes(request):
    if 'uid' not in request.session:
        return redirect("/")
    context = {
        "user": User.objects.get(id=request.session['uid']),
        "user_wishes":Wish.objects.filter(added_by=User.objects.get(id=request.session['uid'])),
        "granted":Wish.objects.filter(granted=True),
        "all_wish":Wish.objects.all()
    }
    return render(request, "wishes.html", context)

def new_wish(request):
    if 'uid' not in request.session:
        return redirect("/")
    return render(request, "new.html")

def create_wish(request):
    if request.method == "POST":
        errors = Wish.objects.wish_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            print("errors have been found")
            return redirect("/wishes/new")
        
        Wish.objects.create(
            name=request.POST['name'],
            description=request.POST['description'],
            added_by=User.objects.get(id=request.session['uid'])
        )
        print("new wish has been created")
    return redirect("/wishes")


def edit_wish(request, w_id):
    context = {
        'wish': Wish.objects.get(id=w_id)
    }
    return render(request, "edit.html", context)

def update_wish(request, w_id):
    if request.method == "POST":
        errors = Wish.objects.wish_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            print("errors have been found")
            return redirect(f"/wishes/{w_id}/edit")
        
        wish = Wish.objects.get(id=w_id)
        wish.name = request.POST['name']
        wish.description = request.POST['description']
        wish.save()
    return redirect("/wishes")


def delete_wish(request, w_id):
    wish = Wish.objects.get(id=w_id)
    wish.delete()
    return redirect("/wishes")

def grant_wish(request, w_id):
    wish = Wish.objects.get(id=w_id)
    wish.granted = True
    wish.save()
    return redirect("/wishes")

def like_wish(request, w_id):
    user = User.objects.get(id=request.session['uid'])
    wish = Wish.objects.get(id=w_id)
    wish.liked_by.add(user)
    return redirect("/wishes")


def unlike_wish(request, w_id):
    user = User.objects.get(id=request.session['uid'])
    wish = Wish.objects.get(id=w_id)
    wish.liked_by.remove(user)
    return redirect("/wishes")

def stats(request):
    if 'uid' not in request.session:
        return redirect("/")
    context = {
        "user": User.objects.get(id=request.session['uid']),
        "user_wishes":Wish.objects.filter(added_by=User.objects.get(id=request.session['uid'])),
        "user_grant":Wish.objects.filter(added_by=User.objects.get(id=request.session['uid']),granted=True),
        "user_pinding":Wish.objects.filter(added_by=User.objects.get(id=request.session['uid']),granted=False),
        "granted":Wish.objects.filter(granted=True),
        "all_wish":Wish.objects.all()
    }
    return render(request, "show_wish.html", context)

def register(request):
    if request.method == "POST":
        errors = User.objects.register_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/")
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(
            password.encode(), bcrypt.gensalt()).decode()  
        print(pw_hash)
        
        new_user = User.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            # birthday=request.POST['birthday'],
            password=pw_hash)
        request.session['uid'] = new_user.id
        return redirect("/wishes")

def login(request):
    if request.method == "POST":
        errors = User.objects.login_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/")
        logged_user = User.objects.get(email=request.POST['email'])
        request.session['uid'] = logged_user.id
        return redirect('/wishes')
    # redirect back to a safe route
    return redirect("/")

def logout(request):
    del request.session['uid'] 
    return redirect('/')