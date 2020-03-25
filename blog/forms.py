from django import forms
from .models import Post, Comments

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','image','description','is_public']

        widgets = {
            'title': forms.TextInput(attrs = {
                'class': 'form-control',
                'placeholder': 'Enter a beautiful title for your post'
            }),

            'description': forms.Textarea(attrs = {
                'class': 'form-control',
                'placeholder': 'Explain your thoughts in brief',
                'rows': '5'
            })
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(attrs = {
                'class': 'form-control',
                'placeholder': 'Add your comment',
                'rows': '3'
            })
        }