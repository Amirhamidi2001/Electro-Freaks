from django import forms
from blog.models import Comment


class CommentForm(forms.ModelForm):
    """
    The CommentForm model is used for processing a Comment form. It is a ModelForm that is based on the Comment model
    """

    class Meta:
        model = Comment
        fields = ["post", "name", "email", "subject", "message"]
