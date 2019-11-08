from django.db import models
from django.template.defaultfilters import slugify


class Event(models.Model):
	name = models.CharField(max_length=256)
	slug = models.SlugField(unique=True,max_length=256)
	date = models.DateTimeField()
	venue = models.CharField(max_length=512)
	image = models.ImageField() 
	description = models.TextField()

	def save(self, *args, **kwargs):
		# generate URL slug whenever saved
		if not self.slug:
			self.slug = slugify(self.name)
			super(Post, self).save(*args, **kwargs)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['-date']
		def __unicode__(self):
			return self.name