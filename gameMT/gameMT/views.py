import os
from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import Context
from django.template import RequestContext
from django.db.models import Q
from django.contrib.auth import models
from forms import UserForm,LoginForm
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from chat.models import ChatRoom

from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt

import json,re

@csrf_exempt
def index(request):
    if request.user.is_authenticated():
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        username = user.first_name + ' ' + user.last_name
        chat_rooms = ChatRoom.objects.order_by('name')[:5]

        if username.isspace():
        	username = user.username
        return render(request, 'index.html', Context({'username': username, 'user_id': user_id, 'chat_list': chat_rooms,}))
    else: # return the "select a forum" page.
        request.session['currUserId'] = -1  # set -1 for anonymous user.
        return render(request, 'index.html', Context({ 'username': 'Visitor', 'user_id': '-1',}))


@csrf_exempt
def logout_view(request): 
    logout(request)
    request.session['currUserId'] = -1
    return HttpResponse(json.dumps({}), content_type='application/json')


@csrf_exempt
def login_view(request):
    response = {}
    username = request.REQUEST.get('username', '')
    password = request.REQUEST.get('password', '')
    if not re.match(r'[^@]+@[^@]+\.[^@]+', username): # valid email address
        user = authenticate(username=username, password=password)
    else: # try user name match
        users = User.objects.filter(email__iexact=username)
        if users.count() != 1:
            return HttpResponse("Your user name and/or password is incorrect.", status=403)
        user = authenticate(username=users[0].username, password=password)
    
    if user:
        login(request, user)
        request.session['currUserId'] = user.id
        response['user_id'] = user.id
        response['user_name'] = user.first_name + ' ' + user.last_name
        
        return HttpResponse(json.dumps(response), mimetype='application/json')
       
    else:
        request.session['currUserId'] = -1
        return HttpResponse("Your user name and/or password is incorrect.", status=403)


@csrf_exempt
def register(request):
    response = {}
    email = request.REQUEST.get('email').lower()
    if User.objects.filter(email=email).count()>0:
    	return HttpResponse("This user already exists; please sign in.", status=403)

    username = email
    password = request.POST['password']
    description = request.POST['userinfo']
    first_name = request.POST['firstname']
    last_name = request.POST['lastname']

    user = User.objects.create_user(username, email, password)
    user.first_name = first_name
    user.last_name = last_name
    user.save()

    user = authenticate(username=username, password=password)

    if user:
    	login(request, user)
        request.session['currUserId'] = user.id
        response['user_id'] = user.id
        response['user_name'] = user.first_name + ' ' + user.last_name
        return HttpResponse(json.dumps(response), content_type='application/json')

    else:
        return HttpResponse("User registered, but login failed.", status=403)
