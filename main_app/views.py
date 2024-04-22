from django.shortcuts import render
from .models import Finch

# Create your views here.

finches = [
  {'common_name': 'House finch', 'species': 'Haemorhous mexicanus', 'description': 'Brown with streaky white breast', 'age': 3, 'sex': 'F'},
  {'common_name': 'House finch', 'species': 'Haemorhous mexicanus', 'description': 'Red head and throat with brown streaky breast', 'age': 2, 'sex': 'M'},
  
  
]

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {
        'finches': finches
    })