# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re, bcrypt
from models import *  
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'python_belt/index.html')

def register(request):
    if request.method =='POST':
        name = request.POST['name']
        user = request.POST['uname']
        hired = request.POST['date']
        password = request.POST['password']
        cpassword = request.POST['confirmpassword']
        flash_errors = False

        if len(password) < 8:
            messages.error(request, "Password must be at least 8 characters")
            flash_errors = True

        #checks passwords match
        if password != cpassword:
            messages.error(request, "Your passwords must match")
            flash_errors = True

        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        
        if name.isalpha():
            pass
        else:
            messages.error(request, "First name cannot have numbers (or spaces)") 
            flash_errors = True

        if len(name) > 3:
            pass
        else:
            messages.error(request, "Name must be over 3 characters!")
            flash_errors = True

        if len(user) > 3:
            pass
        else:
            messages.error(request, "Username must be over 3 characters!")
            flash_errors = True

        try:
            users.objects.get(user_name=user)
            messages.error(request, "User already registered! Or email adddress taken")
            flash_errors = True
        except:
            pass

        if flash_errors is True:
            return redirect('/main')
        else:
            users.objects.create(your_name=name, user_name=user, date_hired=hired, pword=pw_hash)
            return redirect('/main')        
    else:
        return redirect('/main')

def login(request):
    if request.method == 'POST':
        user=request.POST['uname']
        password = request.POST['password']
        user_query = users.objects.get(user_name=user)
        flash_errors = False

        request.session['user']=user_query.id

        if len(user_query.user_name) > 0:
            if bcrypt.checkpw(password.encode(), user_query.pword.encode()) is True:
                pass
            else:
                messages.error(request, 'User name/password combination does not match')
                flash_errors = True
        else:
            messages.error(request,'User name/password combination does not match')
            flash_errors = True

        request.session['name'] = user_query.your_name

        if flash_errors is True:
            return redirect('/main')
        else:
            return redirect('/dashboard')
    else:
        return redirect('/main')

def dashboard(request):
    if 'user' in request.session:
        context={
            'mine':wishes.objects.filter(who=request.session['user']),
            'likes':wishes.objects.filter(fans__id=request.session['user']).exclude(who__id=request.session['user']),
            'not_mine':wishes.objects.exclude(fans__id=request.session['user']).exclude(who__id=request.session['user'])
        }
        return render(request, 'python_belt/dashboard.html', context)
    else:
        return(reverse('test_main'))

def logout(request):
    del request.session['user']
    del request.session['name']
    return redirect('/main')

def create(request):
    if 'user' in request.session:
        return render(request, 'python_belt/create.html')
    else:
        return(reverse('test_main'))

def new(request):
    if request.method =="POST":
        item1 = request.POST['item']
        if len(item1) < 3:
            messages.error(request, "Item must be at least 3 characters")
            return redirect('/wish_list/create')
        else:
            user=users.objects.get(id=request.session['user'])
            new = wishes.objects.create(item=item1, who=user)
            new.save()
            new.fans.add(user)
            return redirect('/wish_list/create')
    else:
        return redirect('/dashboard')

def item(request, id):
    context={
        'top':wishes.objects.get(id=id),
        'users':users.objects.filter(favorite=wishes.objects.get(id=id))
    }
    return render(request, 'python_belt/item.html', context)


def like(request, id):
    top=wishes.objects.get(id=id)
    user = users.objects.get(id=request.session['user'])
    top.fans.add(user)
    return redirect('/dashboard')

def unlike(request, id):
    top=wishes.objects.get(id=id)
    user = users.objects.get(id=request.session['user'])
    top.fans.remove(user)
    return redirect('/dashboard')

def remove(request, id):
    tip = wishes.objects.get(id=id)
    tip.delete()
    return redirect('/dashboard')