from django.shortcuts import render

from django.views.generic import (CreateView, DeleteView, 
                                    DetailView, ListView,UpdateView)
from .models import Todo


class Index(ListView):
    model = Todo
    template_name = 'index.html'
    fields = []

    def get_context_data(self):
        
        context = self.model.objects.all()
        return {'context': context}
