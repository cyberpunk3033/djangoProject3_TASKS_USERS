from .models import Task
from .forms import TaskForm, CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
def task_list(request):
    tasks = Task.objects.order_by('-created_date')
    return render(request, 'task_list.html', {'tasks': tasks})

def create_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'user_create.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('task_list')  # шаблон перехода на страницу
        else:
            error_message = 'Неверные учетные данные'
    else:
        error_message = ''

    return render(request, 'login.html', {'error_message': error_message})
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'create_task.html', {'form': form})

def view_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    return render(request, 'view_task.html', {'task': task})

def update_status(request, task_id):
    task = Task.objects.get(pk=task_id)
    if request.method == 'POST':
        status = request.POST.get('status')
        task.status = status
        task.save()
        return redirect('view_task', task_id)
    return render(request, 'update_status.html', {'task': task})
