from django.db import models

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

