from django.db import models
from django.template.defaultfilters import slugify

class Event(models.Model):
	title = models.CharField(max_length=256)
	slug = models.SlugField(unique=True,max_length=256)
	date = models.DateTimeField()
	image = models.ImageField() 
	content = models.TextField()

	def save(self, *args, **kwargs):
		# generate URL slug whenever saved
		if not self.slug:
			self.slug = sligify(self.title)
			super(Post, self).save(*args, **kwargs)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-date']
		def __unicode__(self):
			return self.title