from email.policy import default
from xmlrpc.client import DateTime
from django.db import models
from django.forms import BooleanField, DateField

# Create your models here.
class Todolist(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    date = models.DateTimeField()
