from django.urls import path
from . import views
urlpatterns = [

    path('aboutus', views.aboutus, name='aboutus'),
    path('accounts/logout', views.logout, name='logout')
]