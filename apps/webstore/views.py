from django.shortcuts import render

# Create your views here.

def kayu(request):
    return render(request, 'index.html')
