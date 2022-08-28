from django.shortcuts import render, HttpResponse
def homework(request):
    return render(request, 'homework.html')

def homework_2(request):
    return HttpResponse ('Добро пожаловать в приложение ToDo - Admin)')