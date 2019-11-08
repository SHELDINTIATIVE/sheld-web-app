from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):
	name = models.CharField(max_length=128)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Category'
		verbose_name_plural = 'Categories'
		ordering = ['name']

		
class Post(models.Model):
	title = models.CharField(max_length=256)
	category = models.ManyToManyField(Category)
	author = models.CharField(max_length=256)
	email = models.EmailField()
	slug = models.SlugField(unique=True, max_length=256, blank=True)
	date = models.DateTimeField(blank=True)
	image = models.ImageField(blank=True)
	content = models.TextField()
	likes = models.IntegerField(default=0)
	page_views = models.IntegerField(default=0)

	def save(self, *args, **kwargs):
		# generate URL slug whenever saved 
		if not self.slug:
			self.slug = slugify(self.title)
			super(Post, self).save(*args, **kwargs)

	def __str__(self):
		title = self.title
		if len(title) > 40:
			title = title[:40] + '...'
		return title 

	class Meta:
		ordering = ['-date']
		def __unicode__(self):
			return self.title


class Comment(models.Model):
	name = models.CharField(max_length=50)
	content = models.TextField()
	posted_on = models.DateTimeField(auto_now_add=True)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)

	def __str__(self):
		content = self.content
		if len(content) > 40:
			content = content[:40] + '...'
		return content

	class Meta:
		ordering = ['-posted_on']
