from django.shortcuts import render, redirect
from django.views.generic import ListView
import requests


def home(request):    
    response = requests.get('http://127.0.0.1:8000/')
    tasks = response.json()
    return render(request, 'home.html', {'tasks':tasks})
    
def create_task(request):   
    if request.method == 'POST':
        data = {     
            "title": request.POST['title'],
            "body": request.POST['body'],
        }
        created = requests.post('http://127.0.0.1:8000/create_task/', data=data)
        
        if created.status_code == 201:
            return redirect('home') 
    return render(request, 'create_task.html')

def manage_task(request, task_id):    
    if request.method == 'POST':
        data = {     
            "title": request.POST['title'],
            "body": request.POST['body'],
        }
        created = requests.put(f'http://127.0.0.1:8000/manage_task/{task_id}/', data=data)
        if created.status_code == 204:
            return redirect('home') 
        
    return render(request, 'manage_task.html')   