from django.shortcuts import render
from homepage.models import blog
from .forms import BlogPosts

# Create your views here.
def home(request):
	all_objects = blog.objects.all();
	template = "home.html"
	form = BlogPosts(request.POST or None)
	if form.is_valid():
		variable = form.save(commit = 'false')
		variable.save()
	context = {
		"form" : form,
		"variable1" : all_objects,
		"variable2" : all_objects[0],
		"variable3" : all_objects[0].title,
	}

	return render(request, template, context)

