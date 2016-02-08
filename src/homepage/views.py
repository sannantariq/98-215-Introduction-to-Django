from django.shortcuts import render
from homepage.models import blog

# Create your views here.
def home(request):
	all_objects = blog.objects.all();
	template = "home.html"
	context = {
		"variable1" : all_objects,
		"variable2" : all_objects[0],
		"variable3" : all_objects[0].title,
	}
	return render(request, template, context)

