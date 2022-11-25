from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import (
                                    CreateView, DeleteView, 
                                    DetailView, ListView,
                                    UpdateView
                                )
from django.http import JsonResponse
from .models import Todo
from .forms import TodoForm
import json


def is_ajax(request):
    return request.headers.get("x-requested-with") == "XMLHttpRequest"


def serializer(model_data):
    
    info = []

    for todo in model_data:
        data = {}
        data['id'] = todo.id
        data['title'] = todo.title
        data['body'] = todo.body
        data['completed'] = todo.completed
        data['created_at'] = todo.created_at
        data['edited_at'] = todo.edited_at
        info.append(data)
    return info


class Index(ListView):

    """
        A view for viewing all todos
    """

    model = Todo
    template_name = 'index.html'
    fields = []
    ordering = ['-created_at']


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


class CompleteTodo(UpdateView):
    """
        A view for setting completed value of a todo
    """
    model = Todo
    fields = ["completed"]

    def form_valid(self, form):
        if is_ajax(self.request):
            todo_id = self.request.POST.get("todo")
            todo = Todo.objects.get(pk=todo_id)
            if todo.completed == False:
                form.instance.completed = True
            else:
                form.instance.completed = False
        return super(CompleteTodo, self).form_valid(form)


def search(request):
    """
        A function to return todo search result
    """

    result = []
    if is_ajax(request):
        if request.POST.get("todo") == 'completed':
            result = Todo.objects.filter(completed=True).order_by('-created_at')
        elif request.POST.get("todo") == 'pending':
            result = Todo.objects.filter(completed=False).order_by('-created_at')
        
        return JsonResponse({
            'data' : serializer(result)
        })
