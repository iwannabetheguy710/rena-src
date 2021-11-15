from django.db import models
from django.contrib.auth.models import *
from home.models import *

# Create your models here.
class Testcase(models.Model):
	test_id = models.AutoField(primary_key=True)
	problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
	inp = models.TextField(max_length=100000, default='')
	out = models.TextField(max_length=100000, default='')
	def __str__(self):
		return f'Problem test case: {self.problem.title}'

class Submission(models.Model):
	submit_id = models.CharField(primary_key=True, max_length=1000)
	problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
	author = models.ForeignKey(Profile, on_delete=models.CASCADE)
	status_code = models.CharField(max_length=5, default='')
	message = models.CharField(max_length=500, default='')
	runtime = models.IntegerField(default=0)
	language = models.CharField(max_length=10, default='C++')
	publish_date = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return f'Submit: \"{self.problem}\" by {self.author}, status {self.status_code}'
