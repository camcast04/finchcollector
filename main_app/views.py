from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Finch
from .forms import FeedingForm

# Create your views here.

# finches = [
#   {'common_name': 'House finch', 'species': 'Haemorhous mexicanus', 'description': 'Brown with streaky white breast', 'age': 3, 'sex': 'F'},
#   {'common_name': 'House finch', 'species': 'Haemorhous mexicanus', 'description': 'Red head and throat with brown streaky breast', 'age': 2, 'sex': 'M'},
  
  
# ]

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {
        'finches': finches
    })
    
def finches_detail (request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    feeding_form = FeedingForm()
    return render(request, 'finches/detail.html', {'finch': finch, 'feeding_form': feeding_form})

class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'
    
class FinchUpdate(UpdateView):
    model = Finch
    fields = ['common_name', 'species', 'sex', 'description', 'age']
    
class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches'
    
