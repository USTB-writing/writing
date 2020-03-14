from django.shortcuts import render

# Create your views here.
def square(request):
	return render(request, 'square/square.html')

