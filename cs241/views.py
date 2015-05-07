from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth import *	
from django.core.context_processors import csrf

def login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('login.html',c)

def auth(request):
	username = request.POST.get('username','')
	password = request.POST.get('username','')
	user = authenticate(username=username, password=password)

	if user is not None:
		login(request, user)
#		return render_to_response('loggedin.html',{'username',request.user.username})
		return HttpResponseRedirect('/account/loggedin/')
	else:
		return HttpResponseRedirect('/account/invalid/')

def loggedin(request):
	if not request.user.is_authenticated:
		return render_to_response('loggedin.html',{'username',request.user.username})
	else:
		return HttpResponseRedirect('/account/login/')

def invalid(request):
	return render_to_response('invalid.html')

def logout(request):
	auth.logout(request)
	s = "successfully logged out"
	return render_to_response('login.html',{'state',s})