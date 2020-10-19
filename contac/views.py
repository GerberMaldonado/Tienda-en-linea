import io
from django.shortcuts import render

# Create your views here.
def contac(request):
    return render(request, 'contac/index.html')