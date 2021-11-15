from django.db import models
from django.contrib.auth.models import *
from martor.models import MartorField

# Create your models here.
class Profile(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE) # reference to user
	ratings = models.DecimalField(default=float(0), decimal_places=2, max_digits=6) # ratings of user
	slogan = models.CharField(default='', max_length=50, blank=True)
	total_problems = models.IntegerField(default=0) # total solved problems
	total_match = models.BigIntegerField(default=0) # total joined contest
	total_win = models.BigIntegerField(default=0) # total contest win
	total_diff = models.CharField(default='0.00', max_length=8) # last status of rating
	total_ratio = models.DecimalField(default=float(0), decimal_places=2, max_digits=5) # ratio of winning rate
	social_facebook = models.CharField(default='', max_length=100, blank=True)
	social_github = models.CharField(default='', max_length=100, blank=True)
	level = models.CharField(max_length=15, default="Level 1") # leveling
	color = models.CharField(max_length=10, default="grey") # levling color
	def __str__(self):
		return self.user.username

rt_choice = tuple((str(x * 100) + '+', str(x * 100) + '+') for x in range(8, 30))

class Problem(models.Model):
	problem_id = models.AutoField(primary_key=True) # problem id
	author = models.ForeignKey(Profile, on_delete=models.CASCADE) # author of problem
	title = models.CharField(max_length=50, default='') # problem title
	statement = models.TextField(max_length=10000, default='') # problem statement
	input_description = models.TextField(max_length=8000, default='') # problem verdict
	output_description = models.TextField(max_length=8000, default='') # problem verdict
	sample_input = models.TextField(max_length=8000, default='\n') # problem sample test
	sample_output = models.TextField(max_length=8000, default='\n') # problem sample output
	time_limit = models.DecimalField(default=float(1.0), decimal_places=3, max_digits=4) # probem timelimit
	memory_limit = models.IntegerField(default=64) #problem memory limit
	tag = models.CharField(choices=rt_choice, max_length=6, default='?') # tag of problem
	accepted_user = models.IntegerField(default=0) # total user accepted
	publish_date = models.DateTimeField(auto_now_add=True) # publish date
	def __str__(self):
		return self.title

class Blog(models.Model):
	entry_id = models.CharField(default='', max_length=50, primary_key=True) # blog id
	author = models.ForeignKey(Profile, on_delete=models.CASCADE) # blog author
	title = models.CharField(max_length=100, default='') # blog title
	content = models.TextField(max_length=30000, default='') # blog content, description
	viewed = models.IntegerField(default=0) # blog viewed
	on_feed = models.BooleanField(default=False) # blog on_feed, if this true, this blog can show on landing page
	publish_date = models.DateTimeField(auto_now_add=True) # blog publish date
	def __str__(self):
		return self.title

class Comment(models.Model):
	comment_id = models.AutoField(primary_key=True) # comment id
	blog = models.ForeignKey(Blog, on_delete=models.CASCADE) # comment on a blog
	author = models.ForeignKey(Profile, on_delete=models.CASCADE) # command author
	comment_description = models.TextField(max_length=25000, default='') # comment content
	upvote = models.IntegerField(default=0) # comment upvote
	publish_date = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return f'Comment (ID: {self.comment_id}): {self.blog} of {self.author}'