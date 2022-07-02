from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('createcard/',views.createcard,name='createcard'),
    path('createcard/addcard/',views.addcard,name='addcard')
]