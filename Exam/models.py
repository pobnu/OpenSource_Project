from django.db import models

class Question(models.Model):
	question = models.CharField(max_length=200)
	option1 = models.CharField(max_length = 200)
	option2 = models.CharField(max_length = 200)
	option3 = models.CharField(max_length = 200)
	option4 = models.CharField(max_length = 200)
	answer = models.CharField(max_length = 200)

# Create your models here.
