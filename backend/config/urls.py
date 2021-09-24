from django.contrib import admin
from django.urls import path

from posts.views import PostsListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', PostsListView.as_view()),
]
