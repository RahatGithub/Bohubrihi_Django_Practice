from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView

# Create your views here.
def index(request):
    context = {'msg' : 'John Wick is a man of word'}
    return render(request, 'main/index.html', context)


# Using class-based view 
class GreetView(TemplateView):
    template_name = 'main/greet.html' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['name'] = "Rahat Ahmed Chowdhury" 
        context['dept'] = "CSE" 
        return context 
