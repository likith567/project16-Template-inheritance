from django.shortcuts import render

# Create your views here.
def boot(request):
    return render(request,'boot.html')

def inheritance(request):
    return render(request,'inheritance.html')
