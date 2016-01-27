from django.shortcuts import render

# Create your views here.

def boot_list(request):
    return render(request, 'DSboot/index.html')