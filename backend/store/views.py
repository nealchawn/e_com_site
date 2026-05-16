#from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def home(request):
  data = {
      'message': 'Welcome to Chawn E-Commerce Store!'
  }
  # return render(request, 'store/home.html',data)
  return JsonResponse(data)