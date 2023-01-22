from django.db import models

# Create your models here.

class Employee(models.Model):
	STATUS = (
			('B.Tech','B.Tech'),
			('M.Tech','M.Tech'),
			('Ph.D','Ph.D'),
		)
	firstname = models.CharField(max_length=200, null=True)
	lastname = models.CharField(max_length=200, null=True)
	email = models.EmailField(max_length=200, null=True)
	password = models.CharField(max_length=50, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	degree = models.CharField(max_length=200, null=True, choices=STATUS)
	program_of_study = models.CharField(max_length=50, null=True)
	graduation_year = models.IntegerField(null=True)

	def __str__(self):
		return self.firstname

	def isExists(self):
		if Employee.objects.filter(email=self.email):
			return True

		return False

	@staticmethod
	
	def get_empby_email(email):

		try:
			return Employee.objects.get(email = email)
		except:
			return False