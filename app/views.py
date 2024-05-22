from django.shortcuts import render
from django.http import HttpResponse


from app.forms import *  #to import all the classes declared in forms.py file in  my application


''''as we use python oops concept here to create input elements
so here we declare an object of our form class so that we can access all the input fields here 
now we pass that object to dictionary so that we can send the object from backend to frontend  '''



'''def studentforms(request):
    ESFO=Student()                  # empty object creation of our form class we declared in forms.py file
    d={'ESFO':ESFO}                 #sending data from backend to frontend
    return render(request,'studentforms.html',d)'''



####### RETRIEVING OF FORM DATA /COLLECTING FORM DATA ##########


def studentforms(request):
    ESFO=Student()                  # empty object creation of our form class we declared in forms.py file
    d={'ESFO':ESFO}                 #sending data from backend to frontend
    if request.method=='POST':
        SDFO=Student(request.POST)   #now collected data will come under the wrapper of formobject  with dictionary request.post having my data where my  wrapper is studentforms--form object
        if SDFO.is_valid():                #is_valid() is to validate the submitted data if valid it returns true else false
            print(SDFO.cleaned_data)        #collected data is stored in cleaned_data list where our key will be input fields and values will be submitted value for that respective input field
            return HttpResponse('Data  Submitted Successfully')
        else:
            return HttpResponse('INVALID DATA')

    return render(request,'studentforms.html',d)
