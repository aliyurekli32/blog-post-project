from django.shortcuts import HttpResponse

def home_page(request):
  return HttpResponse('<button><a href="https://127.0.0.1:8000">Home</a></button><button><a href="https://127.0.0.1:8000/blog">blog</a></button><button><a href="https://127.0.0.1:8000/user">user</a></button>')