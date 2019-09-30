from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
	return HttpResponse("<h1>Hello, world!</h1>")

def render_function(request):
	context = {
	"msg": "Hello World!"
	}
	return render(request, "html_file.html", context)
