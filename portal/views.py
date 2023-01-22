from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from .models import Employee

# Create your views here.

def home(request):
	return render(request,'portal/dashboard.html')

def Login(request):
	if request.method == 'GET':
		return render(request, 'portal/Login.html')
	else:
		email = request.POST.get('email')
		password = request.POST.get('password')
		checker = Employee.get_empby_email(email)
		error_msg = None
		if checker:
			if check_password(password,checker.password):
				return render(request,'portal/postlogin.html',{'Firstname':checker.firstname, 'lastname':checker.lastname, 'email':checker.email, 'degree':checker.degree, 'prog':checker.program_of_study, 'grad':checker.graduation_year});
			else:
				error_msg='Error: Password is incorrect......'
		else:
			error_msg='Error: E-mail doesn\'t exist......'

		return render(request,'portal/Login.html',{'error':error_msg})

def Register(request):
	if request.method == 'GET':
		return render(request, 'portal/Register.html')
	else:
		username = request.POST['uname']
		lastname = request.POST['lname']
		email = request.POST['email']
		password = request.POST['password']
		degree = request.POST['selectD']
		ProgStudy = request.POST['pstudy']
		GradYear = request.POST['gyear']

		NewEntry = Employee(firstname=username, lastname=lastname, email=email, password=password, degree=degree, program_of_study=ProgStudy, graduation_year=GradYear)
		
		error_msg=None
		if NewEntry.isExists():
			error_msg = 'Error: E-mail already registered!!!' 

		if not error_msg:
			NewEntry.password = make_password(NewEntry.password)
			NewEntry.save()	
			return render(request,'portal/postlogin.html',{'Firstname':username, 'lastname':lastname, 'email':email, 'degree':degree, 'prog':ProgStudy, 'grad':GradYear})
		else:
			return render(request,'portal/Register.html',{'error':error_msg})