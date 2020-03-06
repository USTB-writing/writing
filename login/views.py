from django.shortcuts import render

# Create your views here.
# Create your views here.
def home(request):
	return render(request, 'login/login.html')

def register(request):
	return render(request, 'login/register.html')	

def login(request):
	return render(request, 'login/login.html')	