from django.shortcuts import render

def base(request):
    return render(request, 'core/base.html')

# Create your views here.
