from django.shortcuts import render

# Create your views here.
def gallery(request):
    return render(request, 'gallery.html')
def aboutus(request):
    return render(request,'about us.html')
def index(request):
    return render(request,'index.html')
def contact(request):
    return render(request,'contact.html')