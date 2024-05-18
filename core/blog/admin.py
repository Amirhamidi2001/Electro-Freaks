from django.contrib import admin
from blog.models import *


class PostAdmin(admin.ModelAdmin):
    """
    This class is for displaying the post model in the admin interface.
    """

    date_hierarchy = "created_date"
    empty_value_display = "-empty-"
    list_display = ("title", "author", "status", "created_date")
    list_filter = ("status",)
    search_fields = ("title", "contect")


class CommentAdmin(admin.ModelAdmin):
    """
    This class is for displaying the contact model in the administration
    """

    date_hierarchy = "created_date"
    empty_value_display = "-empty-"
    list_display = ("post", "name", "approved", "subject", "created_date")
    list_filter = ("post", "name")
    search_fields = ("name", "subject")


admin.site.register(Category)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)
