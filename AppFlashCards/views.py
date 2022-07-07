from dataclasses import dataclass
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render,HttpResponse
import random

from AppFlashCards.models import Data

# Create your views here.
def getdata():
    all_data = Data.objects.all()
    db_data = []
    for dt in all_data:
        temp = {'id':dt.id,'question':dt.question,'answer':dt.answer,'tag':dt.tag}
        db_data.append(temp)
    return db_data
 
def index(request):
   db_data = getdata()
   return render(request,"index.html",{'db_data':db_data})


def createcard(request):
    return render(request,"createcard.html")

def addcard(request):
    if request.method == 'POST':
        model = Data()
        model.question = request.POST['question']
        model.answer = request.POST['answer']
        model.tag = request.POST['tag']
        model.save()
        db_data = getdata()
        return redirect("/",{'db_data':db_data})
    return HttpResponseRedirect("Unable to add to database")

def show(request,id):
    db_data = getdata()
    for d in db_data:
        if d['id'] == id:
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
            return render(request,'index.html',{'db_data':db_data})
    return HttpResponse("Unable to delete")
from django.template import RequestContext


def handler404(request,exception):
    return render(request,'404.html')