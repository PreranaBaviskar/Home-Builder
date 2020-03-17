from django.shortcuts import render
from .models import heading

# Create your views here.
def index(request):

    titles = heading.objects.all()
    return render(request, 'index.html', {'title': titles})
