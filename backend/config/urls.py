from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from posts.views import PostsListView, PostDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', PostsListView.as_view()),
    path('posts/<int:pk>/', PostDetailView.as_view()),
]
urlpatterns += staticfiles_urlpatterns()

