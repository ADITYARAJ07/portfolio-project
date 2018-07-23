from django.shortcuts import render, get_object_or_404

from .models import Blog

def allblog(request):
	blogs= Blog.objects
	return render(request,'blogs/allblog.html',{'blogs':blogs})
	
def detail(request,blog_id):
	detailblog=get_object_or_404(Blog, pk=blog_id)
	return render(request, 'blogs/detail.html', {'blog':detailblog})
	