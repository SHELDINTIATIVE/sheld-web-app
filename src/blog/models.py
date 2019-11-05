from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):
	name = models.CharField(max_length=128)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Category'
		verbose_name_plural = 'Categories'
		order = ['name']

		
class Post(models.Model):
	title = models.CharField(max_length=256)
	category = models.ManyToManyField(Category)
	author = models.CharField(max_length=256)
	slug = models.SlugField(unique=True,max_length=256)
	date = models.DateTimeField()
	image = models.ImageField()
	content = models.TextField()
	likes = models.IntegerField(default=0)
	page_views = models.IntegerField(default=0)

	def save(self, *args, **kwargs):
		# generate URL slug whenever saved 
		if not self.slug:
			self.slug = slugify(self.title)
			super(Post, self).save(*args, **kwargs)

	def __str__(self):
		title = self.name
		if title.len() > 40:
			title = title[:40] + '...'
		return title + ' by ' + self.author 

	class Meta:
		ordering = ['-date']
		def __unicode__(self):
			return self.title


class Comment():
	name = models.CharField(max_length=50)
	content = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)

	def __str__(self):
		content = self.content
		if content.len() > 40:
			content = content[:40] + '...'
		return content + ' by ' + self.name

	class Meta:
		ordering = ['-date']
