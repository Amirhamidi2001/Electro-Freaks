from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from datetime import datetime
from django.views import View

from blog.models import Category, Post, Comment
from blog.forms import CommentForm


class BlogView(View):
    def get(self, request, **kwargs):
        posts = Post.objects.filter(status=1)
        if kwargs.get("cat_name") != None:
            posts = posts.filter(category__name=kwargs["cat_name"])
        if kwargs.get("tag_name") != None:
            posts = posts.filter(tags__name__in=[kwargs['tag_name']])
        if kwargs.get("author_username") != None:
            posts = posts.filter(author__username=kwargs["author_username"])
        if kwargs.get("date") != None:
            date_str = kwargs["date"]
            date = datetime.strptime(date_str, '%Y-%m-%d').date()
            posts = posts.filter(date=date)
        posts = Paginator(posts, 20)
        try:
            page_number = request.GET.get("page")
            posts = posts.get_page(page_number)
        except PageNotAnInteger:
            posts = posts.get_page(1)
        except EmptyPage:
            posts = posts.get_page(1)
        context = {"posts": posts}
        return render(request, "blog/blog.html", context)


class SingleView(View):
    def get(self, request, pid):
        posts = Post.objects.filter(status=1)
        post = get_object_or_404(posts, pk=pid)
        post.counted_views += 1
        post.save()
        comments = Comment.objects.filter(post=post.id, approved=True)
        form = CommentForm
        context = {"post": post, "comments": comments, "form": form}
        return render(request, "blog/single-blog.html", context)

    def post(self, request, pid):
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(
                request, messages.SUCCESS, "نظر شما با موفقیت ارسال شد"
            )
        else:
            messages.add_message(request, messages.ERROR, "نظر شما ثبت نشد")
        return self.get(request, pid)


class BlogSearch(View):
    def get(self, request, **kwargs):
        posts = Post.objects.filter(status=1)
        if request.method == "GET":
            if s := request.GET.get("s"):
                posts = posts.filter(content__contains=s)
        context = {"posts": posts}
        return render(request, "blog/blog.html", context)
