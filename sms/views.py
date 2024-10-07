from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,template_name='smsytem\index.html')

def product(request):
    return render(request,template_name='smsytem\product.html')

def productdetails(request):
    return render(request,template_name='smsytem\productdetails.html')