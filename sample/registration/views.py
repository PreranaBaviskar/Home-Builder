from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.
def register(request):

    if request.method == 'POST':
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'User exits')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email exists')
                return redirect('register')
            else:
                user=User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password1)
                user.save()
                print('User created')
                return redirect('login')

        else:
            messages.info(request, 'Password not matching')
            return redirect('register')
        #return redirect('/')

    else:
        return render(request, 'register.html')


