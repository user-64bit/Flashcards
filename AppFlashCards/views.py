from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render,HttpResponse

from AppFlashCards.models import Data

# Create your views here.

def index(request):
    all_data = Data.objects.all()
    db_data = []
    for dt in all_data:
        temp = {'question':dt.question,'answer':dt.answer,'tag':dt.tag}
        db_data.append(temp)
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
        return HttpResponse("OK let's see")
    return HttpResponse("Didn't work")