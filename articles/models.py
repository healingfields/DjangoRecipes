from django.db import models

# Create your models here.
class Article(models.Model):

    title = models.CharField(max_length=25)
    content = models.TextField(max_length=155,blank=True,null=True)
    published = models.BooleanField(default=True)