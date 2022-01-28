from django.shortcuts import render, redirect
from .models import Task
from django.views import View
from .forms import TaskForm
# Create your views here.

class MainView(View):
    def get(self, request):
        tasks = Task.objects.all()

        form = TaskForm
        context = {'tasks': tasks, 'form': form}
        return render(request, "TODO/index.html", context)

    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")


class TaskView(View):
    def get(self, request, id):
        task = Task.objects.get(id=id)
        form = TaskForm(instance=task)
        context = {"task": task, "form": form}
        return render(request, "TODO/task.html", context)

    def post(self, request, id):
        task = Task.objects.get(id=id)
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("/")


def Delete(request, id):
    task = Task.objects.get(id=id)

    if request.method == "POST":
        task.delete()
        return redirect("/")

    context = {'task': task}
    return render(request, "TODO/delete.html", context)

