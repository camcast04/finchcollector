from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    #path for finches index (see all of them)
    path('finches/', views.finches_index, name='index')
]
