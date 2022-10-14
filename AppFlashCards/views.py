from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render,HttpResponse
import random
from django.urls import reverse
from AppFlashCards.forms import flashcardsform
from AppFlashCards.models import Data

# Create your views here.
def getdata():
    all_data = Data.objects.all()
    db_data = []
    for dt in all_data:
        temp = {'id':dt.id,'question':dt.question,'answer':dt.answer,'tag':dt.tag,'choice':dt.choice}
        db_data.append(temp)
    return db_data
 
def index(request):
   db_data = getdata()
   for d in db_data:
    d['tag'] = d['tag'].upper()
   return render(request,"index.html",{'db_data':db_data})


def createcard(request):
    form = flashcardsform(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request,"createcard.html",{"form":form})
    # return render(request,"createcard.html")


def addcard(request):
    if request.method == 'POST':
        model = Data()
        model.question = request.POST['question']
        model.answer = request.POST['answer']
        model.tag = request.POST['tag'].lower()
        choice = 1
        if request.POST.get('code') == 'on':
            choice = 0
        model.choice = choice
        model.save()
        db_data = getdata()
        return redirect("/home",{'db_data':db_data})
    return HttpResponseRedirect("Unable to add to database")

def show(request,id):
    db_data = getdata()
    for d in db_data:
        if d['id'] == id:
            d['tag'] = d['tag'].upper()
            return render(request,'show.html',{'db_data':[d]})
    return HttpResponse("Unable to show")


def memorize(request):
    db_data = getdata()
    random.shuffle(db_data)
    if len(db_data) == 0:
        return HttpResponse("Add cards to memorize")
    return render(request,'memorize.html',{'db_data':db_data[0]})

def delete(request,id):
    db_data = getdata()
    for d in db_data:
        if d['id'] == id:
            task = Data.objects.get(id=id)
            task.delete()
            db_data = getdata()
            return HttpResponseRedirect(reverse('index'))
    return HttpResponse("Unable to delete")


def handler404(request,exception):
    return render(request,'404.html')

def search(request):
    q = request.GET['search-text']
    search_data = Data.objects.filter(tag=q.lower())
    if len(search_data)==0:
        return HttpResponse("There is not data available for searched item")
    return render(request,'search.html',{'db_data':search_data})

def edit(request,id):
    obj = get_object_or_404(Data, id = id)
    form = flashcardsform(request.POST or None, instance = obj) 
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("Done")
    return render(request, "update_card.html",{'form':form,'id':id})

def updatecard(request,id):
    if request.method == 'POST':
        question = request.POST['question']
        answer = request.POST['answer']
        tag = request.POST['tag'].lower()
        choice = 1
        if request.POST.get('code') == 'on':
            choice = 0
        
        model = Data.objects.get(id=id)
        model.question = question
        model.answer = answer
        model.tag = tag
        model.choice = choice
        model.save()
        db_data = getdata()
        return redirect("/home",{'db_data':db_data})
    return HttpResponseRedirect("Unable to add to database")

def login(request):
    return render(request,'login.html')

def authenticate(request):
    if request.method == 'POST':
        with open("./AppFlashCards/creadentials.txt") as f:
            uname = f.readline()
            passw = f.readline()
        uname = uname.split(':')[1].strip()
        passw = passw.split(':')[1].strip()
        print(uname,passw)
        if(request.POST['username']==uname and request.POST['password']==passw):
            return redirect("/home")
        
        return HttpResponse("Wrong Creadentials")

def signup(request):
    return render(request, 'signup.html')

def register(request):
    if request.method == 'POST':
        u_name = request.POST['username']
        passw = request.POST['password']
        c_passw = request.POST['confirm_password']

        if passw != c_passw:
            return HttpResponse("Password did not match with confirm password!")
        else:
            u = 'username:'+u_name
            p = '\npassword:'+passw
            with open("./AppFlashCards/creadentials.txt","w") as f:
                f.writelines([u,p])
            return redirect("/login")
