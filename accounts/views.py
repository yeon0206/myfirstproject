from django.shortcuts import render

# Create your views here.
def home(request):
    name = 'Hello'
    args={
        'myName' : name
    }
    return render(request, 'accounts/login.html', args)