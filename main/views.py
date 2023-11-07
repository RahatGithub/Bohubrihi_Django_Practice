from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {'msg' : 'John Wick is a man of word'}
    return render(request, 'main/index.html', context)