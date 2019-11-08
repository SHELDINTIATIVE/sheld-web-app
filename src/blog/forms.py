from django import forms

from . models import Post, Comment


class NewPostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['author', 'title', 'category', 'email', 'image', 'content']
		widgets = {
			'category': forms.SelectMultiple(attrs={'size':10}),
			'content': forms.Textarea(attrs={'rows':10}),
		}


class NewCommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['post', 'name', 'content']
		widgets = {
			'content': forms.Textarea(attrs={'rows':12}),
		}