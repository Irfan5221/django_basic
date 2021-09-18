from django.db import models

# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    contact=models.CharField(max_length=12)
    desc=models.TextField()
    datetime=models.DateTimeField()

    #display name on database for send message

    def __str__(self):
        return self.name
