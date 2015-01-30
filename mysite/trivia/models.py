import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Question(models.Model):
	date_open = models.DateField(primary_key=True)
	question_text = models.CharField(max_length=200)
	answer_text = models.CharField(max_length=200)
	
	def is_open(self):
		return self.date_open == timezone.now().date()

	def __str__(self):              # __unicode__ on Python 2
		return self.question_text

class MyUser(models.Model):
	user = models.OneToOneField(User, primary_key=True)
	num_correct = models.IntegerField(default=0)
	num_total = models.IntegerField(default=0)
	last_answered = models.DateField(null=True)

