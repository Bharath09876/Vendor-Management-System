from django.shortcuts import render

# Create your views here.
def landing_page(request):
  
  return render(request,'login.html')

def login(request):
  
  return render(request,'login.html')

def tracking_home(request):
  
  return render(request,'tracking.html')

def home(request):
  
  return render(request,'index.html')

def register_main(request):
  
  return render(request,'register.html')