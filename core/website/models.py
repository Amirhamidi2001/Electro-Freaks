from django.db import models


class Contact(models.Model):
    """
    This class is for users to contact the admin
    """

    name = models.CharField(max_length=60)
    email = models.EmailField()
    subject = models.CharField(max_length=60)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_date"]

    def __str__(self):
        return self.name


class Newsletter(models.Model):
    """
    This class is for website newsletter
    """

    email = models.EmailField()

    def __str__(self):
        return self.email
