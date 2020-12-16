from django.shortcuts import render,redirect
from .models import Password
import requests
import json


# Create your views here.

def login_view(request):
    if request.method == 'POST':
        data= request.POST
        payload = {'username': data['username'], 'password': data['password']}
        r = requests.post("https://recruitment.fisdev.com/api/login/", data=payload)
        token =r.json()
        instance = Password()
        instance.passkey = token['token']
        instance.save()
        return redirect('home')
    else:
        return render(request,'core/login.html')


    

def home(request):
    #log in api call
    
    if request.method == 'POST':
        obj= request.POST
        mydict= {}

        mydict=obj.dict()

        url = "https://recruitment.fisdev.com/api/v1/recruiting-entities/"
        payload = {
        "name": mydict['username'],
        "email": "taskin.cse14@gmail.com",
        "phone": mydict['phone'],
        "full_address": mydict['address'],
        "name_of_university": mydict['university'],
        "graduation_year": mydict['graduation'],
        "cgpa": mydict['cgpa'],
        "experience_in_months": mydict['exp'],
        "current_work_place_name": mydict['workplace'],
        "applying_in": mydict['apply'],
        "expected_salary": mydict['salary'],
        "field_buzz_reference": mydict['reference'],
        "github_project_url": mydict['github'],
        "cv_file": {
        "tsync_id": "be96f0e188a6de73b186c043-7365-4605-85eb-76021f16803f"
            }
        }
        #data submission api
        result_token = str('Token')+" "+ str(Password.objects.get(id=1))
        headers = {'content-type': 'application/json','Authorization':result_token}
        res = requests.post(url, data= json.dumps(payload), headers=headers)
        cv_id= res.json()
        value=cv_id['cv_file']['id']

        #cv submission api
        url2= f"https://recruitment.fisdev.com/api/file-object/{value}/"
        cv =  request.FILES['cv']
        files = {'file': cv.read(),'boundary':''}
        headers = {'content-type': 'multipart/form-data;boundary=buj51jbhybhyv251taskin','Authorization':result_token}
        response = requests.put(url2,files=files, headers=headers)
        print(response.content)
        

    return render(request,'core/base.html')


