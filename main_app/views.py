from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Finch, ShinyObject
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
    
def add_feeding(request, finch_id):
  # create a ModelForm instance using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the finch_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.finch_id = finch_id
    new_feeding.save()
  return redirect('detail', finch_id=finch_id)


class ShinyObjectList(ListView):
  model = ShinyObject

class ShinyObjectDetail(DetailView):
  model = ShinyObject

class ShinyObjectCreate(CreateView):
  model = ShinyObject
  fields = '__all__'

class ShinyObjectUpdate(UpdateView):
  model = ShinyObject
  fields = ['name', 'material']

class ShinyObjectDelete(DeleteView):
  model = ShinyObject
  success_url = '/shiny_objects'