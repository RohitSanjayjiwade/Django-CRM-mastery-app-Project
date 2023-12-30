from django.shortcuts import render, redirect, get_object_or_404

from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required

from django.contrib import messages

from .models import Record

# Create your views here.


# Homepage

def index(request):

	return render(request, 'webapp/index.html')


# Register a user

def register(request):

	form = CreateUserForm()

	if request.method == 'POST':

		form = CreateUserForm(request.POST)

		if form.is_valid():

			form.save()

			messages.success(request, "Account created successfully!")

			return redirect("my_login")



	return render(request, 'webapp/register.html', {'form': form})


# - Login a user

def my_login(request):

	form = LoginForm()

	if request.method == 'POST':

		form = LoginForm(data=request.POST)

		if form.is_valid():

			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:

				auth.login(request, user)

				messages.success(request, "You have logged!")

				return redirect("dashboard")

	return render(request, 'webapp/my-login.html', {'form': form})


# - Dashboard

@login_required(login_url='my_login')
def dashboard(request):

	my_records = Record.objects.all()

	return render(request, 'webapp/dashboard.html', {'records': my_records})


# - Create a record

def create_record(request):
	form = CreateRecordForm()
	print("boyy")

	if request.method == 'POST':
		print("okkk")

		form = CreateRecordForm(request.POST)

		if form.is_valid():

			form.save()

			messages.success(request, "Your record was created successfully!")

			return redirect("dashboard")

	return render(request, 'webapp/create-record.html', {'form': form})


# - update a record

@login_required(login_url='my_login')
def update_record(request, id):

	record = Record.objects.get(id=id)

	form = UpdateRecordForm(instance=record)

	if request.method == 'POST':

		form = UpdateRecordForm(request.POST, instance=record)

		if form.is_valid():

			form.save()

			messages.success(request, "Your record was updated successfully!")

			return redirect("dashboard")

	return render(request, 'webapp/update-record.html', {'form': form})


# - Read / View a singular record

@login_required(login_url='my_login')
def view_record(request, id):

	record = Record.objects.get(id=id)

	return render(request, 'webapp/view-record.html', {'record': record})


# - Delete a record

@login_required(login_url=my_login)
def delete_record(request, id):

	record = get_object_or_404(Record, id=id)

	record.delete()
	messages.success(request, "Your record was deleted successfully!")

	return redirect("dashboard")





# - Logout a user

def user_logout(request):

	auth.logout(request)

	messages.success(request, "Logout successfully!")

	return redirect("my_login")


