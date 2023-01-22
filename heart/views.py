from django.shortcuts import render ,redirect ,HttpResponseRedirect
from .models import *
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth import authenticate ,login ,logout
import pandas as pd
import numpy as np
from .forms import *

# Create your views here.


##############################################################3
#                              HOME PAGE VIEW       # #######3
##############################################################

def index(request):
    doctors =Doctors.objects.all()[:5]
    articles = Article.objects.all()[:5]
    context ={'doctors':doctors , "articles":articles}
    return render(request , 'heart/index.html' , context)


#___________________________________________________***************************______________________________#







# ############################################################
#          Disease Predciton View             ###########
#############################################################

def prediction_view(request):
    if request.method == 'POST':
        name=request.POST['name']
        age =int(request.POST['age'])
        sex=int(request.POST['sex'])
        cp=int(request.POST['cp'])
        trestbps =int(request.POST['trestbps'])
        chol=int(request.POST['chol'])
        fbs=int(request.POST['fbs'])
        restecg=int(request.POST['restecg'])
        max_heart_rate=int(request.POST['max_heart_rate'])
        exang =int(request.POST['exang'])
        oldpeak =float(request.POST['oldpeak'])
        slope =int(request.POST['slope'])
        print(name , age , sex , cp , trestbps , chol , fbs , restecg,max_heart_rate , exang ,oldpeak ,slope)
        pateint_data = Diseases(name=name,age=age,sex=sex,cp=cp,trestbps=trestbps,chol=chol,fbs=fbs,restecg=restecg,max_heart_rate=max_heart_rate,exercise_angina=exang,oldpeak=oldpeak,slope=slope)
        pateint_data.save()
    
        return HttpResponseRedirect(f'/patient_report/{pateint_data.pk}')

    return render(request,'prediction/prediction.html')

#___________________________________________________***************************______________________________#










#######################################################################
## PAtient Report After prediction View
#######################################################################

def patient_report(request ,pk):
    patient = Diseases.objects.get(pk=pk)

    if patient.target == 1:
        patient.target = 'Cardiovascular Diseases'
    else:
        patient.target  = "No Heart Diseases"
        
    if patient.sex == 0:
        patient.sex = 'Female'
    else:
        patient.sex = "Male"
    return render(request,'prediction/patient_report.html', {'patient':patient})

#___________________________________________________***************************______________________________#







# ####################################################
#        Disease Details View
######################################################

def cardio(request):
    return render (request , 'heart/cardio.html')



#___________________________________________________***************************______________________________#










# ##########################################
# About Page View
############################################
def about(request):
    return render(request,'heart/about.html')

#___________________________________________________***************************______________________________#










# #######################################################
#  Display All Article Views
##########################################################

class ListArticles(ListView):
    model = Article
    template_name = "article/article.html"

#___________________________________________________***************************______________________________#





# #######################################################     
#            Article Detail View                        #   
#########################################################    

class DetailArticle(DetailView):
    model = Article
    template_name="article/article_detail.html"

#___________________________________________________***************************______________________________#






# #######################################################
#  Display All Doctors Views
##########################################################

class DoctorsList(ListView):
    model = Doctors
    template_name = "doctors/doctors.html"
#___________________________________________________***************************______________________________#









# #######################################################
#            Doctor Detail View
##########################################################

class DoctorsDetail(DetailView):
    model = Doctors
    template_name = 'doctors/doctors_detail.html'
    context_object_name = 'doctor'

#_____________________________***************************______________________________#





def contact_view(request):
    return render(request,'heart/contact.html')



def commingsoon(request):
    return render(request,'soon.html')








def SignUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignUpForm()
        context = {'form':form}
        return render(request, 'accounts/signup.html',context)




def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username , password=password)
        if user is not None:
            login(request , user)
            return redirect('/profile/')
    form = LoginForm()
    return render(request ,'accounts/login.html' ,{'form':form})



def logout_view(request):
    logout(request)
    return redirect('/')



def profile(request):
    return render (request , 'accounts/profile.html')



















