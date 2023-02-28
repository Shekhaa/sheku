from django.shortcuts import render, redirect
from django.http.request import HttpRequest
from home.models import tile
from django.http import HttpResponse

# Create your views here.
def index(request):
    if request.method=="POST":
        lists=[1,2,3,4,5,6,7,8,9,10]
        
        lists[0]=eval(request.POST.get('ob1'))
        lists[1]=eval(request.POST.get("ob2"))
        lists[2]=eval(request.POST.get("ob3"))
        lists[3]=eval( request.POST.get("ob4"))
      #  lists[4]=eval(request.POST.get("ob5"))
       # lists[5]=eval( request.POST.get("ob6"))
        #lists[6]=eval(request.POST.get('ob7'))
        #lists[7]=eval(request.POST.get("ob8"))
        #lists[8]=eval(request.POST.get("ob9"))
        #lists[9]=eval( request.POST.get("ob10"))

        print(lists)
        dicts=dict(enumerate(lists))
        print(dicts)
        context={'dicts':dicts}
        return render(request,'show.html',context)

    return render(request, 'index.html')
 
def Carts(request):
    var=tile.objects.all()
    #chalo ek site ka sara maal nikalte hain
    kar={'la':var}
    return render(request,'Carts.html',kar)

