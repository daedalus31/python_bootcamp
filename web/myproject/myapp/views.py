from django.http import HttpResponse
from django.shortcuts import render


def hello_view(request, name):
    return HttpResponse(f'Hello {name}!')


def arithmetic_view(request, operation, num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    if operation == 'add':
        res = num1 + num2
    elif operation == 'sub':
        res = num1 - num2
    else:
        res = 'Bad operation!'
    return render(request=request, template_name='operacja.html',
                  context={'wynik': res})
