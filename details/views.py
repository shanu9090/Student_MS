from django.shortcuts import render,HttpResponseRedirect
from . models import Student
from django.http import HttpResponse

# Create your views here.
def homepage(req):
    return render (req,"details/homepage.html")

def fillform(req):

    if req.method=="POST":
        print(req.POST)
        nam=req.POST.get('nm')
        # if not nam.isalpha():
            # msg="Invalid input"
            # return render(req,"details/fillform.html",{'msg':msg})
        emai=req.POST.get('email')
        addres=req.POST.get('add')
        age=req.POST.get('age')
        mobilep=req.POST.get('phone')
        image=req.FILES.get('img')
        instance=Student(name=nam,email=emai,address=addres,age=age,mobile=mobilep,image=image)
        instance.save()
    return render (req,"details/fillform.html")

def fetchdetail(req):
    d=Student.objects.all()
    return render (req,"details/fetchdetail.html",{'data':d})

def update(req,id):
    if req.method=="POST":
        nam=req.POST.get('nm')
        emai=req.POST.get('email')
        addres=req.POST.get('add')
        age=req.POST.get('age')
        mobilep=req.POST.get('phone')
        image=req.FILES.get('img')
        if image==None:
            Student.objects.filter(id=id).update(name=nam,email=emai,address=addres,age=age,mobile=mobilep)
            return HttpResponseRedirect("/fetchdetail/")
        else:
           new_data=Student(id=id ,name=nam,email=emai,address=addres,age=age,mobile=mobilep,image=image)
           new_data.save()
           return HttpResponseRedirect("/fetchdetail/")
      
    data=Student.objects.get(pk=id)
    return render(req,"details/update.html",{'data':data})



def delete(req,id):
    d=Student.objects.get(pk=id)
    d.delete()
    return HttpResponseRedirect('/fetchdetail/')
   # return HttpResponse("Data is  Deleted")
    #return render (req,"details/sdelete.html")         

