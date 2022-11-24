from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import (CreateView, DeleteView, 
                                    DetailView, ListView,UpdateView)
from .models import Todo
from .forms import TodoForm


class Index(ListView):

    """
        A view for viewing all todos
    """

    model = Todo
    template_name = 'index.html'
    fields = []


class CreateTodoView(CreateView):
    """
        A view for creating a todo
    """

    model = Todo
    success_url = reverse_lazy('index')
    form_class = TodoForm
    template_name = 'forms/create_todo.html'

    def form_valid(self, form):
        return super(CreateTodoView, self).form_valid(form)


class TodoView(DetailView):
    """
        A view for creating a todo
    """

    model = Todo
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class EditTodo(UpdateView):
    """
        A view for updating a todo
    """
    model = Todo
    template_name = 'forms/edit.html'
    fields = ['title', 'body']


class DeleteTodo(DeleteView):
    """
        A view for deleting a todo
    """
    model = Todo
    template_name = 'forms/delete.html'
    fields = []
    success_url = reverse_lazy('index')

