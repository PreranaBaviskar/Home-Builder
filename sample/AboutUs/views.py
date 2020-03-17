from django.shortcuts import render,redirect
from .models import info
from django.contrib.auth.models import auth
# Create your views here.
def aboutus(request):
    photo = info.objects.all()
    return render(request, 'aboutus.html', {'photos' : photo})

def logout(request):
    auth.logout(request)
    return redirect('/')
