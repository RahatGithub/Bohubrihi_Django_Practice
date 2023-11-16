from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    # path('greet', views.GreetView.as_view(), name="greet"),
    path('greet', views.ShowMusicians.as_view(), name="greet")
]