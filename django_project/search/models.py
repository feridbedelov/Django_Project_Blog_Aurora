from django.db import models
from django.contrib.auth.models import User


class SearchQuery(models.Model):
    user=models.ForeignKey(User,null=True,blank=True,on_delete=models.SET_NULL)
    query =models.CharField(max_length=220)
    timestamp=models.DateTimeField(auto_now_add=True)


