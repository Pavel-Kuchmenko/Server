from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    id = models.CharField(primary_key=True ,max_length=32)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="posts", on_delete=models.CASCADE)
    pub_date = models.DateTimeField('publish date')
    title = models.CharField(max_length=200)
    content = models.TextField()
