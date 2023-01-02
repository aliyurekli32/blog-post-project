from django.shortcuts import HttpResponse

def home_page(request):
  return HttpResponse('<button><a href="http://127.0.0.1:8000">Home</a></button><button><a href="http://127.0.0.1:8000/api/blog/">blog</a></button><button><a href="http://127.0.0.1:8000/category/">category</a></button>')