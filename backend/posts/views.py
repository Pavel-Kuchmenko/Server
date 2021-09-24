from posts.models import Post
from django.http import HttpResponse, HttpRequest
from django.views.generic import ListView
from .models import Post

# Create your views here.
class PostsListView(ListView):
    model = Post
    template_name = 'posts/index.html'
