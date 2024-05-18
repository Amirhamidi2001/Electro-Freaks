from django.contrib import admin
from website.models import Contact, Newsletter


class ContactAdmin(admin.ModelAdmin):
    """
    This class is for displaying the contact model in the administration
    """

    date_hierarchy = "created_date"
    empty_value_display = "-empty-"
    list_display = ("name", "email", "subject", "created_date")
    list_filter = ("name",)
    search_fields = ("name", "subject")


admin.site.register(Contact, ContactAdmin)
admin.site.register(Newsletter)
