from django import template
from blog.models import Post, Category

register = template.Library()


@register.inclusion_tag("blog/blog-recent-posts.html")
def latest_posts():
    return {"posts": Post.objects.filter(status=1).order_by("-published_date")[:3]}


@register.inclusion_tag("blog/blog-categories.html")
def categories():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category=name).count()
    return {"categories": cat_dict}


@register.inclusion_tag("blog/blog-tags.html")
def tags():
    posts = Post.objects.filter(status=1)
    tags = set()
    for post in posts:
        for tag in post.tags.all():
            tags.add(tag)
    return {'tags': tags}