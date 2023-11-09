from django.shortcuts import render

# Create your views here.
def onefile(request):
    return render(request,'onefile.html')

def twofile(request):
    return render(request,'twofile.html')

def threefile(request):
    return render(request,'threefile.html')

def fourfile(request):
    return render(request,'fourfile.html')

