from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    image = models.ImageField(upload_to='images/posts')

    def get_production_date(self):
        return self.created_date.strftime("%Y-%m-%d")


    def __str__(self):
        return f'{self.title} - {self.id}'