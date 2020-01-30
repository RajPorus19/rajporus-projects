from django.shortcuts import render
from django.http import HttpResponse

posts = [
	{
		'author':'Porus',
		'title':'Blog post',
		'content':'First post content',
		'date_posted':'26/01/2020'
	},
	{
		'author':'Asma',
		'title':'Cutie\'s post',
		'content':'her post content',
		'date_posted':'27/01/2020'
	}

]

def home(request):
	context = {
	'posts' : posts
	}
	return render(request,'app1/home.html',context)

def about(request):
	return render(request, "app1/about.html", {"title" : "about"})
