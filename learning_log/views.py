from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.

def test(request):
	"""A simple Test"""
	return render(request,'learning_log/Test.html')
