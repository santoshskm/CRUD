from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DetailView,DeleteView
from crudpro_app.models import Student
# Create your views here.
class List(ListView):
    model = Student
    template_name = 'list.html'
class Create(CreateView):
    model = Student
    template_name = 'create.html'
    fields = ('__all__')
class Update(UpdateView):
    model = Student
    template_name = 'update.html'
    fields = ('__all__')
