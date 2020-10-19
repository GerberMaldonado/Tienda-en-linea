import io
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.template import loader

# Create your views here.
def home(request):
    return render(request, 'home/index.html')