from django.shortcuts import render
from Mapp.models import movie,update
from Mapp.forms import Mappform
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
# from Mapp.forms import

# Create your views here.
def home(request):
    l=movie.objects.all()
    return render(request,'home.html',{'l':l})



def add(request):
    form=Mappform()
    return render(request,'add.html',{'f':form})



def add1(request):
    if(request.method=="POST"):
        t=request.POST['t']
        d=request.POST['d']
        m=request.FILES['m']

        a=movie.objects.create(title=t,director=d,img=m)
        a.save()
        return home(request)
    return render(request,'add1.html')



def add(request):
    f=Mappform()
    if(request.method=="POST"):
        f=Mappform(request.POST,request.FILES)#form object
        if(f.is_valid()):#oroo values correct aanon nokaan
            f.save()
            return home(request)
        return render(request,'add.html',{'f':f})


# def view(request,p):
#     v=Mapp.objects.get(id=p)
#     return render(request,'view.html',{'v':v})

def edit_film(request,p):
    v=movie.objects.get(id=p)
    f=Mappform(instance=v)
    if(request.method=="POST"):
        print(request.POST)
        f=Mappform(request.POST,request.FILES,instance=v)

    if(f.is_valid()):
        f.save()
        return home(request)
    return render(request,'add.html',{"f":f})

def delete_film(request,p):
    v=movie.objects.get(id=p)
    v.delete()
    return home(request)
