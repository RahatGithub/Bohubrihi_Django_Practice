from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('musicians', views.ShowMusicians.as_view(), name="musicians"),
    path('musician_update/<pk>/', views.UpdateMusician.as_view(), name="musician_update")
]