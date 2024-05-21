from django.shortcuts import render


from app.forms import *  #to import all the classes declared in forms.py file in  my application


''''as we use python oops concept here to create input elements
so here we declare an object of our form class so that we can access all the input fields here 
now we pass that object to dictionary so that we can send the object from backend to frontend  '''



def studentforms(request):
    ESFO=Student()                  #object creation of our form class we declared in forms.py file
    d={'ESFO':ESFO}                 #sending data from backend to frontend
    return render(request,'studentforms.html',d)
