from django.db import models
from django.urls import reverse

# Create your models here.
class List(models.Model):
    title = models.CharField(max_length=140)
    description = models.TextField(blank=True, null=True)
    date = models.DateField()
    due_date = models.DateTimeField()
    done = models.NullBooleanField()

    def get_absolute_url(self):
        return reverse("list:list-detail", kwargs={"id": self.id})
