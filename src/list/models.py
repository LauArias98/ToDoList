from django.db import models


# Create your models here.
class List(models.Model):
    title = models.CharField(max_length=140)
    description = models.TextField(blank=True, null=True)
    date = models.DateField()
    due_date = models.DateTimeField()
    done = models.NullBooleanField()
