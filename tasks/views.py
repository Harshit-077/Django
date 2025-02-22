from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

#tasks = []

class newTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    #priority = forms.IntegerField(label = "Priority",min_value=1,max_value=4)
# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []

    return render(request,"tasks/index.html",{
        #"tasks":tasks
        "tasks":request.session["tasks"] #for maintaining sessions because declaring global variable makes everyone to view your tasks
    })
def add(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    if request.method == "POST":
        form = newTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"].append(task)
            request.session.modified = True
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request,"tasks/add.html",{
                "form":form
            })
    return render(request,"tasks/add.html",{
    "form":newTaskForm()
    })
    