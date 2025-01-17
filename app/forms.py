#for creating django forms and model forms we need to create a forms.py file in our application
#forms.Form in this F should be capital of form that we are inheriting in our class from forms class

from django import forms  # for using forms we need to import it from forms class


class Student(forms.Form):
    Student_name=forms.CharField()    #for taking textfield as input 
    Student_age=forms.IntegerField(min_value=5)    #for taking number field as input where you can specify minimum value and maximum value also according to your need these are optional
    Student_email=forms.EmailField()                #for taking email as input
    Student_url=forms.URLField()                    #for taking url as input
    Student_dob=forms.DateField()                    #for taking date as input in yyyy-mm-dd format
    Student_password=forms.CharField(widget=forms.PasswordInput)   #as no password field  is their so we need to convert charfield to passwordfield using widget=forms.PasswordInput
    Student_address=forms.CharField(widget=forms.Textarea)         #as no password field  is their so we need to convert charfield to textarea using widget=forms.textarea
    Student_address=forms.CharField(widget=forms.Textarea(attrs={'rows':10,'cols':5}))  #as no password field  is their so we need to convert charfield to textarea using widget=forms.textarea we can specify the area of textbox using attrs dictionary by giving rows and columns
    #Submitted_at=forms.DateTimeField()                            #to take input for both time in hh:mm and date in yyyy-mm-dd
    #Submitted_at=forms.TimeField()                            #to take input for  time in hh:mm
    
