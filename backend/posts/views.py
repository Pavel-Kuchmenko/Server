from posts.models import Post
from django.http import HttpResponse, HttpRequest
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
class PostsListView(ListView):
    model = Post
    template_name = 'posts/index.html'

    def get(self, request):
        return super().get(request)

    def get_context_data(self, **kwargs) -> dict:
        return super().get_context_data(**kwargs)

class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/detail.html'
