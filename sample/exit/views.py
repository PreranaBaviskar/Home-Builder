from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth
from .models import entry
# Create your views here.
def login(request):

    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid Credentials")
            return redirect('login')

    else:
        log = entry.objects.all()
        return render(request, 'login.html', {'log' : log})