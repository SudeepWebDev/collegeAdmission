from django.shortcuts import render

def loginForm(request):
    return render(request,'index.html')