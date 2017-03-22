from django.db import models
from django.contrib.auth import login
from django.contrib.auth.signals import user_logged_in

# Create your models here.
# users and items are for single 

class User(models.Model):
	userid = models.CharField(max_length=30,primary_key=True)
	username = models.CharField(max_length=30)
	password = models.CharField(max_length=30)
	email = models.CharField(max_length=50)

	#it is for printing out with normal words
	def _unicode_(self):
		return self.name


class Items(models.Model):
	userid=models.ForeignKey(User)
	itemsid=models.CharField(max_length=30,primary_key=True)
	itemname= models.CharField(max_length=100)
	comments = models.CharField(max_length=254)
	ratings = models.CharField(max_length=30)
	decision=models.BooleanField(default=False)

	def _unicode_(self):
		return self.name


#Groups and boards contained user and items
class Groups(models.Model):
	"""docstring for Groups"""
	groupid = models.CharField(max_length=30,primary_key=True)
	userid = models.ForeignKey(User)
	groupname = models.CharField(max_length=30)

	def _unicode_(self):
		return self.name

		
