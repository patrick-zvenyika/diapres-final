from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import *
from django.db.models import Q
from .forms import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
import pickle
import json
from collections import Counter
from math import ceil
from django.http import JsonResponse
from util.charts import months, colorPrimary, colorSuccess, colorDanger, generate_color_palette, get_year_dict
import csv
import numpy as np
from  django.db.models.functions import ExtractMonth, ExtractYear
import calendar 
from django.db.models import Count

# Create your views here.
#...........................................................#
#Landing Page
#...........................................................#

def Home(request):
    return render(request,'landingpage.html')

#...........................................................#
#Authentication Pages
#...........................................................#

#Login Page
def Login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist!')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('login')
        else:
            messages.error(request, 'Username Or Password does not exist!')
    return render (request, 'auth-signin.html')


#Logout Page
def Logout(request):
    logout(request)
    return redirect('home')

#...........................................................#
#Main Page
#...........................................................#

@login_required(login_url='login')
def Index(request):
    total = PatientData.objects.count()
    total2 = EarlyDiagnosisPatient.objects.count()
    patient_count = total + total2

    pos1 = PatientData.objects.filter(status="Positive").count()
    pos2 = EarlyDiagnosisPatient.objects.filter(status="Positive").count()
    pos = pos1 + pos2

    neg1 = PatientData.objects.filter(status="Negative").count()
    neg2 = EarlyDiagnosisPatient.objects.filter(status="Negative").count()
    neg = neg1 + neg2

    

  
    context = {
        'patient_count':patient_count,
        'pos':pos,
        'neg':neg,
    
    }
    return render(request, 'index.html', context)

#...........................................................#
#Statistic Page
#...........................................................#
@login_required(login_url='login')
def get_filter_options(request):
    grouped_purchases = PatientData.objects.annotate(year=ExtractYear("created_at")).values("year").order_by("-year").distinct()
    options = [purchase["year"] for purchase in grouped_purchases]

    return JsonResponse({
        "options": options,
    })

@login_required(login_url='login')
def get_generalpatient_chart(request, year):
    patients = PatientData.objects.filter(created_at__year=year)
    grouped_patients = patients.annotate(month=ExtractMonth("created_at")).values("month").annotate(count=Count("id_number")).values("count","month")
    
    patient_dict = get_year_dict()

    for group in grouped_patients:
        patient_dict[months[group["month"]-1]] = (group["count"])


    return JsonResponse({
        "title": f"Patients in {year}",
        "data": {
            "labels": list(patient_dict.keys()),
            "datasets": [{
                "label": "Total Patients",
                "backgroundColor": colorPrimary,
                "borderColor": colorPrimary,
                "data": list(patient_dict.values()),
            }],
            
        },
    })


@login_required(login_url='login')
def general_status_chart(request, year):
    purchases = PatientData.objects.filter(created_at__year=year)

    return JsonResponse({
        "title": f"Payment success rate in {year}",
        "data": {
            "labels": ["Non Diabetic", "Diabetic"],
            "datasets": [{
                "label": "Total Patients",
                "backgroundColor": [colorSuccess, colorDanger],
                "borderColor": [colorSuccess, colorDanger],
                "data": [
                    purchases.filter(status='Negative').count(),
                    purchases.filter(status='Positive').count(),
                ],
            }]
        },
    })


@login_required(login_url='login')
def generalstats(request):

    return render(request, 'stats/general-diagnosis.html',{})



@login_required(login_url='login')
def get_filter_options_early(request):
    grouped_purchases = EarlyDiagnosisPatient.objects.annotate(year=ExtractYear("created_at")).values("year").order_by("-year").distinct()
    options = [purchase["year"] for purchase in grouped_purchases]

    return JsonResponse({
        "options": options,
    })

@login_required(login_url='login')
def get_earlydiagnosis_chart(request, year):
    patients = EarlyDiagnosisPatient.objects.filter(created_at__year=year)
    grouped_patients = patients.annotate(month=ExtractMonth("created_at")).values("month").annotate(count=Count("id_number")).values("month", "count")
    
    patient_dict = get_year_dict()

    for group in grouped_patients:
        patient_dict[months[group["month"]-1]] = (group["count"])


    return JsonResponse({
        "title": f"Patients in {year}",
        "data": {
            "labels": list(patient_dict.keys()),
            "datasets": [{
                "label": "Total Patients",
                "backgroundColor": colorPrimary,
                "borderColor": colorPrimary,
                "data": list(patient_dict.values()),
            }],
            
        },
    })

@login_required(login_url='login')
def get_early_males(request,year):
    males = EarlyDiagnosisPatient.objects.filter(created_at__year=year)
    grouped_males = males.annotate(month=ExtractMonth("created_at")).values("month").annotate(males=Count("status"=="Male")).values("month","males")

    males_dict = get_year_dict()

    for i in grouped_males:
        males_dict[months[i["month"]-1]] = [i["males"]]
    
    return JsonResponse({
        "title": f"Patients in {year}",
        "data": {
            "labels": list(males_dict.keys()),
            "datasets": [{
                "label": "Total Patients",
                "backgroundColor": colorPrimary,
                "borderColor": colorPrimary,
                "data": list(males_dict.values()),
            }],
        },
    })

@login_required(login_url='login')
def early_status_chart(request, year):
    purchases = EarlyDiagnosisPatient.objects.filter(created_at__year=year)

    return JsonResponse({
        "title": f"Payment success rate in {year}",
        "data": {
            "labels": ["Non Diabetic", "Diabetic"],
            "datasets": [{
                "label": "Total Patients",
                "backgroundColor": [colorSuccess, colorDanger],
                "borderColor": [colorSuccess, colorDanger],
                "data": [
                    purchases.filter(status='Negative').count(),
                    purchases.filter(status='Positive').count(),
                ],
            }]
        },
    })




@login_required(login_url='login')
def earlystats(request):
    
    return render(request, 'stats/early-diagnosis.html',{})


#...........................................................#
#Chat Page
#...........................................................#
@login_required(login_url='login')
def Chat(request):
    users = User.objects.all()
    message = ChatMessage.objects.all().order_by('-created_at')
    msg_obj = ChatMessage.objects.count()
    paginator = Paginator(message, 6)
    page = request.GET.get('page')
    try:
        msg = paginator.page(page)
    except PageNotAnInteger:
        msg = paginator.page(1)
    except EmptyPage:
        msg = paginator.page(paginator.num_pages)
    
    context = {
        'msg':msg,
        'msg_obj':msg_obj,
        'users':users
    }
    return render(request, 'chat/chat.html', context)

@login_required(login_url='login')
def StartChat(request,id):
    users = User.objects.all()
    user = request.user
    seluser = User.objects.get(id=id)
    prof = User.objects.get(id=seluser.id)
    chats = ChatMessage.objects.all()

    form = ChatMessageForm()
   

    if request.method == 'POST':
        form = ChatMessageForm(request.POST, request.FILES)
        if form.is_valid():
            message = form.save(commit=False)
            message.msg_sender  = request.user
            message.msg_receiver = prof
            message.save()
            return redirect('start-chat', id=seluser.id)
       
    context = {
        'form':form,
        'seluser':seluser,
        'prof':prof,
        'users':users,
        'chats':chats,
        'user':user
    }
    return render(request, 'chat/detail-chat.html', context)

    
#...........................................................#
#Diagnosis Pages
#...........................................................#

#Early-Diagnosis Page
@login_required(login_url='login')
def Diagnosis(request):
    return render(request, 'diagnosis/early-diagnosis.html')

@login_required(login_url='login')
def DiagnosisResult(request):

    model = pickle.load(open('C:/Users/Patrick Zvenyika/Desktop/web2/models/working-model.pkl','rb'))
    
    # age = 47
    # gender = 1
    # polyuria = 1
    # polydipsia = 0
    # sudden = 0
    # weakness = 1
    # polyphagia = 1
    # genital = 0
    # visual = 1
    # itching = 1
    # irrita = 1
    # delayed = 1
    # partial = 0
    # muscle = 1
    # alopecia = 1
    # obesity = 1
    age = int(request.GET['n17'])
    gender = str(request.GET['n2'])
    polyuria = str(request.GET['n3'])
    polydipsia = str(request.GET['n4'])
    sudden = str(request.GET['n5'])
    weakness = str(request.GET['n6'])
    polyphagia = str(request.GET['n7'])
    genital = str(request.GET['n8'])
    visual = str(request.GET['n9'])
    itching = str(request.GET['n10'])
    irrita = str(request.GET['n11'])
    delayed = str(request.GET['n12'])
    partial = str(request.GET['n13'])
    muscle = str(request.GET['n14'])
    alopecia = str(request.GET['n15'])
    obesity = str(request.GET['n16'])

    
    if gender =='Female':
        a2 = 0
    else:
        a2 = 1
    
    if polyuria == 'No':
        a3 = 0
    else:
        a3 = 1
    
    if polydipsia == 'No':
        a4 = 0
    else:
        a4 = 1

    if sudden == 'No':
        a5 = 0
    else:
        a5 =1
    
    if weakness == 'No':
        a6 = 0
    else:
        a6 = 1
    
    if polyphagia == 'No':
        a7 = 0
    else:
        a7 =1
    
    if genital == 'No':
        a8 = 0
    else:
        a8 =1

    if visual == 'No':
        a9 = 0
    else:
        a9 =1

    if itching == 'No':
        a10 = 0
    else:
        a10 = 1

    if irrita == 'No':
        a11 = 0
    else:
        a11 = 1

    if delayed =='No':
        a12 = 0
    else:
        a12 = 1

    if partial == 'No':
        a13 = 0
    else:
        a13 =1

    if muscle == 'No':
        a14 = 0
    else:
        a14 = 1

    if alopecia == 'No':
        a15 = 0
    else:
        a15 = 1

    if obesity == 'No':
        a16 = 0
    else:
        a16 = 1
    

    #gender,polyuria,polydipsia,sudden,weakness,polyphagia,genital,visual,itching,irrita,delayed,partial,muscle,alopecia,obesity
    
    pred = model.predict([[age,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16]])
    predres = " "
    if pred == ['Positive']:
        predres = "Positive"
    else:
        predres = "Negative"
    
    context = {
        'predres':predres
    }
    return render(request, 'diagnosis/early-diagnosis.html', context)


#General-Diagnosis Page
@login_required(login_url='login')
def GDiagnosis(request):
    return render(request, 'diagnosis/general-diagnosis.html')

@login_required(login_url='login')
def GeneralDiagnosis(request):
    modelx = pickle.load(open('C:/Users/Patrick Zvenyika/Documents/GitHub/web/models/model.pkl','rb'))

    va1 = float(request.GET['n1'])
    va2 = float(request.GET['n2'])
    va3 = float(request.GET['n3'])
    va4 = float(request.GET['n4'])
    va5 = float(request.GET['n5'])
    va6 = float(request.GET['n6'])
    va7 = float(request.GET['n7'] )
    va8 = float(request.GET['n8'])

    pred = modelx.predict([[va1,va2,va3,va4,va5,va6,va7,va8]])

    result2 = ""
    if pred == [1]:
        result2 = "Positive"
    else:
        result2 = "Negative"
    
    context = {
        'result2':result2,
    }
    return render(request, 'diagnosis/general-diagnosis.html',context)



#...........................................................#
#Patient DataTables
#...........................................................#

#Early Diagnosis DataTable
@login_required(login_url='login')
def TableList(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    queryset =EarlyDiagnosisPatient.objects.filter(
        Q(name__icontains=q)
    )
    op_obj = EarlyDiagnosisPatient.objects.count()
    paginator = Paginator(queryset, 10)
    page = request.GET.get('page')
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    context = {
        'patient_list':data,
        'op_obj' : op_obj
    }
    return render(request, 'datalist/early-diagnosis.html', context)


#General Diagnosis DataTable
@login_required(login_url='login')
def DataTable(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    queryset =PatientData.objects.filter(
        Q(name__icontains=q)
    )
    op_obj = PatientData.objects.count()
    paginator = Paginator(queryset, 10)
    page = request.GET.get('page')
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    context = {
        'patient_list':data,
        'op_obj' : op_obj
    }
    return render(request, 'datalist/general-diagnosis.html', context)



#...........................................................#
#New Patients
#...........................................................#

#Early Diagnosis
@login_required(login_url='login')
def NewData(request):
    if request.method == 'POST':
        data = EarlyDiagnosisPatient.objects.create(
            name = request.POST.get('name'),
            id_number= request.POST.get('idnumber'),
            gender = request.POST.get('n2'),
            address= request.POST.get('address'),
            contact= request.POST.get('contact'),
            age= request.POST.get('n1'),
            polyuria= request.POST.get('n3'),
            polydipsia= request.POST.get('n4'),
            sudden_weight_loss= request.POST.get('n5'),
            weakness= request.POST.get('n6'),
            polyphagia= request.POST.get('n7'),
            genital_thrush= request.POST.get('n8'),
            visual_blurring= request.POST.get('n9'),
            itching= request.POST.get('n10'),
            irritability= request.POST.get('n11'),
            delayed_healing= request.POST.get('n12'),
            partial_paresis= request.POST.get('n13'),
            muscle_stiffness= request.POST.get('n14'),
            alopecia= request.POST.get('n15'),
            obesity= request.POST.get('n16'),
            height= request.POST.get('height'),
            mass= request.POST.get('mass'),
            status = request.POST.get('result')
        )
    return render(request, 'new details/early-diagnosis.html')

#General Diagnosis
@login_required(login_url='login')
def NewlyData(request):
    if request.method == 'POST':
        data = PatientData.objects.create(
            name = request.POST.get('name'),
            address = request.POST.get('address'),
            id_number = request.POST.get('name2'),
            contact = request.POST.get('contact'),
            pregnancies = request.POST.get('pregnancies'),
            glucose_level = request.POST.get('glucose'),
            blood_pressure = request.POST.get('bp'),
            skin_thickness = request.POST.get('skin'),
            insulin = request.POST.get('insulin'),
            BMI = request.POST.get('bmi'),
            Diabetes_Pedigree_Function = request.POST.get('dpf'),
            age = request.POST.get('age'),
            height = request.POST.get('height'),
            mass = request.POST.get('mass'),
            sex = request.POST.get('gender'),
            status = request.POST.get('outcome')
        )
    return render(request, 'new details/general-diagnosis.html')



#...........................................................#
#SingleDataView Page
#...........................................................#

def SingleData(request, id):
   patient = EarlyDiagnosisPatient.objects.get(id=id)
   context = {
    'patient':patient
   }
   return render(request, 'single-details/early-diagnosis.html', context)

def SingleView(request, id):
    patient = PatientData.objects.get(id=id)
    context = {
        'patient':patient
    }
    return render(request, 'single-details/general-diagnosis.html', context)

#...........................................................#
#Report Generation
#...........................................................#
@login_required(login_url='login')
def gen_single_report(request):
    patients = PatientData.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=general-patient-table.csv'
    writer = csv.writer(response)
    writer.writerow(['Name','Id Number','Gender','Address','Contact','Pregnancies','Glucose Level','Blood Pressure','Skin Tickness','Insulin Level','BMI','Diabetes Pedigree Function','Age','Height','Mass','Status','Created Time'])
 
    for patient in patients:
        writer.writerow([
        patient.name,patient.id_number,patient.sex,patient.address,patient.contact,patient.pregnancies,
        patient.glucose_level,patient.blood_pressure,patient.skin_thickness,patient.insulin,patient.BMI,
        patient.Diabetes_Pedigree_Function,patient.age,patient.height,patient.mass,patient.status,
        patient.created_at
        ])
    return response

@login_required(login_url='login')
def early_single_report(request):
    patients = EarlyDiagnosisPatient.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=early-patient-table.csv'
    writer = csv.writer(response)
    writer.writerow(['Name','Id Number','Gender','Address','Contact','Age','Polyuria','Polydipsia','Polyphagia','Sudden Weight Loss','Weakness','Genital Thrush','Visual Blurring','Itching','Irritability','Delayed Healing','Partial Paresis','Muscle Stiffness','Alopecia','Obesity','Height','Mass','Created Time'])

    for patient in patients:
        writer.writerow([
            patient.name,patient.id_number,patient.gender,patient.address,patient.contact,patient.age,
            patient.polyuria,patient.polydipsia,patient.polyphagia,patient.sudden_weight_loss,patient.weakness,
            patient.genital_thrush,patient.visual_blurring,patient.itching,patient.irritability,
            patient.delayed_healing,patient.partial_paresis,patient.muscle_stiffness,patient.alopecia,
            patient.obesity,patient.height,patient.mass,patient.created_at
        ])

    return response

#...........................................................#
#Delete Record
#...........................................................#
@login_required(login_url='login')
def del_single_gen(request, id):
    patient = PatientData.objects.get(id=id)
    patient.delete()
    context = {
        'patient':patient
    }
    return render(request, 'datalist/general-diagnosis.html', context)

@login_required(login_url='login')
def del_early_gen(request,id):
    patient = EarlyDiagnosisPatient.objects.get(id=id)
    patient.delete()
    context = {
        'patient':patient
    }
    return render(request,'datalist/early-diagnosis.html', context)
