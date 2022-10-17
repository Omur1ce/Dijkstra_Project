from django.shortcuts import render, redirect
from django.contrib import messages

from users.models import SavedRoutes
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your account has been created! You are now able to Login :)')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form': form})

def home(request):
	context = {
        'user': User.objects.all()}
	return render(request, 'home.html', context)
	

@login_required
def profile2(request, username):
	
	user = User.objects.get(username)

	context = {'user': user}
	return render(request, 'profile.html', context)

@login_required
def profile(request):
	return render(request, 'users/profile.html')

def timetable(request):
	pass