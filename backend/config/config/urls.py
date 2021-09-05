from django.contrib import admin
from django.urls import path

from .test_view import foo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('foo/', foo),
]
