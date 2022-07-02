from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render,HttpResponse

from AppFlashCards.models import Data

# Create your views here.
def getdata():
    all_data = Data.objects.all()
    db_data = []
    for dt in all_data:
        temp = {'question':dt.question,'answer':dt.answer,'tag':dt.tag}
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