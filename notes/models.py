from django.db import models
from ckeditor.fields import RichTextField


class Note(models.Model):
	title = models.CharField(max_length=100)
	content = RichTextField()
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return str(self.title)