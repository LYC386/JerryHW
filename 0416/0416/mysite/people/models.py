from django.db import models
class Name(models.Model):
	name = models.CharField(max_length=30)
	birthday = models.DateField(auto_now=False, auto_now_add=False)
	gender_options = (
		('man','男'),
		('woman','女'),
		('other','其他'),
		)
	gender=models.CharField(max_length=20,choices=gender_options)

	def __str__(self):
		return self.name



# Create your models here.
