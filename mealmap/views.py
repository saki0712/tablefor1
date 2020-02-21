from django.views import generic
from .models import Category, Shop
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(generic.ListView):
    model = Shop
    
class DetailView(generic.DetailView):
    model = Shop
    
class UpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    model = Shop
    fields = '__all__'
    
class CreateView(LoginRequiredMixin, generic.edit.CreateView):
    model = Shop
    fields = '__all__'
    
class DeleteView(LoginRequiredMixin, generic.edit.DeleteView):
    model = Shop
    success_url = reverse_lazy('mealmap:index')