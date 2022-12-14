from django.contrib import admin
from django.db import models
from django.contrib.auth.models import *
class Sity(models.Model):
    title = models.CharField(max_length=60)
    def __str__(self):
        return self.title

class Users(models.Model):
    first_name = models.CharField(max_length=50,null=False)
    email = models.EmailField(max_length=40,null=False, primary_key=True)

    def __str__(self):
        return self.email

class Industrial(models.Model):
    title = models.CharField(max_length=40,primary_key=True)

class Agent(models.Model):
    first_name = models.CharField(max_length=30)
class Chat(models.Model):
    doner = models.ForeignKey(User,on_delete=models.CASCADE , related_name='doner')
    recip = models.ForeignKey(User,on_delete=models.CASCADE, related_name='recip')
    message = models.CharField(max_length=40)

    def __str__(self):
        return str(self.doner) + " " + str(self.recip) + " " +  str(self.message)
admin.site.register([Chat, Agent])


