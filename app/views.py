from django.shortcuts import render

# Create your views here.
def usd_filters(request):
    d={"var":'Hi hArsHaD How aRE YOU'}
    return render(request,'usd_filters.html',d)