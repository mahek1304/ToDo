from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

def index(request):
    tasks = Task.objects.all()                              # for grabbing all the models
    form = TaskForm()

    if request.method == 'POST':                            # meaning, we actually want to create something
        form = TaskForm(request.POST)                       # value will be passed to TaskForm & that val will be saved
        if form.is_valid():
            form.save()                                     # will save it to the database
        return redirect('/')                                # sending it to the same url path (since the same template needs to be 
                                                            # returned)
    
    context = {'tasks':tasks, 'form':form}                  # context dict is created, tasks are passed in it and this dict is then 
                                                            # passed to render function
    return render(request, 'tasks/list.html', context)      # Thus context is here the third parameter

def updateTask(request, pk):                                # with request, we are throwing a dynamic url path, ie we are throwing a pk
    task = Task.objects.get(id = pk)                        # for grabbing the item, the id will be grabbed from the url pattern 
                                                            # (thats how we will retrieve an object)
    form = TaskForm(instance = task)                        # if we just pass a form , it will give us a blank form 
                                                            # but coz the instance is of the object, so it has to be of same model, 
                                                            # so it will prefill that form first
    
    if request.method == 'POST':  
        form = TaskForm(request.POST, instance = task)      # we need to throw the instance too, if we leave the request.POST just like
                                                            # the previous form, it will create a new itam even though it has the old
                                                            # item's isntance, So even though we are throwing the new data(request.POST)
                                                            # we are updating its instance (instance = task)   
        if form.is_valid():
            form.save()
        return redirect('/')      
    context = {'form': form}
    return render(request, 'tasks/update_task.html', context)

def deleteTask(request, pk):
    item = Task.objects.get(id = pk)                        # in the template we are looking for the item, thus we need to pass it here,
                                                            # otherwise it will give an error
    if request.method == 'POST': 
        item.delete()
        return redirect('/')
    
    context = {'item':item}
    return render(request, 'tasks/delete.html', context)