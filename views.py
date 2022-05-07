
from django.shortcuts import render
from os import name
import cv2
from django.contrib.messages.api import MessageFailure
from django.http import HttpResponse, request
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout 
from django.core.mail import send_mail, EmailMessage
import pandas as pd
from certigen.admin import service_PariticipantAdmin

from certigen.models import service_Pariticipant

# Create your views here.


def certificategen(request):
    
    if request.method=="POST":
           
       if cv2.form.is_valid():
            
            par_name = request.POST.get('par_name')
            text_file = request.FILES.get('text_file')
            template = request.FILES.get('template')
            email = request.POST.get('email')
        
            service = service_Pariticipant(
			    par_name = par_name,
			    text_file=text_file,
                template = template,
			    email=email
		    	)
            service.save()
            
            template = cv2.imread("certificate-template.jpg")
            cv2.putText(template, name.strip(), (210,415), cv2.FONT_HERSHEY_SIMPLEX, 2.1, (250 , 0, 0), 5, cv2.LINE_AA)
            cv2.imwrite(f'generated-certificate-data/{name}.jpg',template)
            
            messages.success(request, "Certificate is generated at generated-certificate-data!") 
               
            return render(request, "submitform.html")
