from django.db import models

# Create your models here.

class info(models.Model):
    text = models.TextField(max_length=200, default="now")
    title = models.TextField(max_length=200, default="here")
    image = models.ImageField(upload_to='pics')

from django.db import models

# Create your models here.
