from django.db import models
from django.contrib.auth.models import User #Make data unique to each user
# Create your models here.

class Topic(models.Model):
	"""Topic the user is entering"""
	text = models.CharField(max_length = 200)
	date_added = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)	#establishes a relationship between topic and user model

	def __str__(self):
		"""Return a string representation of the model."""
		return self.text

class Entry(models.Model):
	"""Specifics learned about a topic."""
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE) #on topic delete, delete all models associated
	#Foreign key is simple a key that connects an entry to a specific topic, Each topic has a specific key/ID upon creation
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add =True)

	class Meta:
		verbose_name_plural = 'entries'

	def __str__(self):
		"""Return a string representation of the model."""
		return f"{self.text[:50]}...."