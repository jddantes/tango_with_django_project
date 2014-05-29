from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
	context = RequestContext(request)
	context_dict = {'boldmessage': "I am bold font from the context"}
	return render_to_response('rango/index.html', context_dict, context)

def about(request):
	# return HttpResponse("Rango says: Here is the About page <br/><a href='/rango'>Home</a>") # Does not use template
	context = RequestContext(request)
	context_dict = {}
	return render_to_response('rango/about.html', context_dict, context)