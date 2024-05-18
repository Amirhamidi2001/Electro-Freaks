from django.urls import path
from .views import BlogView, SingleView, BlogSearch

app_name = "blog"

urlpatterns = [
    path('', BlogView.as_view(), name='blog'),
    path('post/<int:pid>/', SingleView.as_view(), name='single'),
    path('search/', BlogSearch.as_view(), name='search'),
    path('category/<str:cat_name>/', BlogView.as_view(), name='category'),
    path('tag/<str:tag_name>/', BlogView.as_view(), name='tag'),
    path('author/<str:author_username>/', BlogView.as_view(), name='author'),
    path('date/<str:date>/', BlogView.as_view(), name='date'),
]
