from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateField(auto_now_add=True)