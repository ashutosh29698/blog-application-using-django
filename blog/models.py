from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 50)
    description = models.TextField()
    image = models.ImageField(blank=True, upload_to='pics')
    date_posted = models.DateTimeField(auto_now_add = True)
    is_public = models.BooleanField(default = True)

    def __str__(self):
        return self.title

class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    commented_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_commented = models.DateTimeField(auto_now_add=True)