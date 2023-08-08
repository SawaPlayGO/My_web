from django.shortcuts import render


def top_sellers(request):
    return render(request, 'top-sellers.html')

def marmelads(request):
    return render(request, 'index.html')

def logining(request):
    return render(request, 'logining.html')
