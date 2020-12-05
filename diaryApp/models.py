from django.db import models
import datetime
from django.contrib.auth.models import User
# Create your models here.
class Memory(models.Model):
    content = models.TextField(blank=True,null=True)
    date = models.DateField(("Date"), default=datetime.date.today)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date',]
    

    def __str__(self):
        return self.content
    

