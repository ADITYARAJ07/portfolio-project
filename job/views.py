from django.shortcuts import render

from .models import Job

from qualification.models import Qualification

def home(request):
	jobs = Job.objects
	qual = Qualification.objects
	return render(request, 'jobs/home.html', {'jobs': jobs,'quals': qual})
	
def about(request):
	return render(request, 'jobs/about.html')
