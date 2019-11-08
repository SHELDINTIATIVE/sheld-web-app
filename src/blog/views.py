from django.shortcuts import render
from django.views.generic import (
	ListView,
	FormMixin
	)

from . models import Post, Comment
from . forms import NewCommentForm


class PostListView(ListView):
	model = Post
	context_page_name = 'posts'
	paginate_by = 10
	template_name = 'blog/post_list.html'


class PostDetailView():
	model = Post
	form_class = NewCommentForm
	template_name = 'blog/post_detail.html'

	def get_context_data(self, **kwargs):
		context = super(PostDetailView, self).get_context_data(**kwargs)
		context['form'] = NewCommentForm(initial={'post': self.object})
		return context

	def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(PostDetailView, self).form_valid(form)