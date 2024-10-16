from django.http.response import HttpResponse
from django.http.request import HttpRequest

import random

def hello_view(request: HttpRequest) -> HttpResponse:
  return HttpResponse("Hello, World!")

def roll_die_view(request: HttpRequest) -> HttpResponse:
  roll = random.randint(1,6)
  return HttpResponse(f'This was the dice you rolled! {roll}')