from django.http.response import HttpResponse
from django.http.request import HttpRequest

def hello_view(request: HttpRequest):
  return HttpResponse("Hello Students")