from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
    #return HttpResponse("Rango says hello world!")# Create your views here.
    context = RequestContext(request)
    context_dict = {'boldmessage': "I am bold font from the context - lol"}
    return render_to_response('rango/index.html', context_dict, context)



def about(request):
    #return HttpResponse("Rango says hello world!")# Create your views here.
    context = RequestContext(request)
    context_dict = {'boldmessage': "stop messing l"}
    return render_to_response('rango/about.html', context_dict, context)

