from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem
# Create your views here.

def todoView(request):
    items = TodoItem.objects.all()

    #return HttpResponse('<em>This</em> is <br> A todo app')
    return render(request, 'todo.html', {'all_items':items})

def addTodo(request):
    #Create a new todo item and saved it
    content = request.POST['content'] #Find the attribute that has the name of 'content'
    new_item = TodoItem(content=content)
    #save
    new_item.save()
    #Redirect the browser to '/todo/'
    return HttpResponseRedirect('/todo/')

def deleteTodo(request, todo_id):
    item_to_delete = TodoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todo/')
