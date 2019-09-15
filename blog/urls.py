from django.urls import path
from .views import index, single
urlpatterns = [
    path('', index, name="blog_index"),
    path('<str:slug>/', single, name="blog_single")
]
