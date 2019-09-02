from django.db import models

class Instagram(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	username = models.CharField(max_length=100)

	def __str__(self):
		return "{}.{}".format(self.id, self.username)