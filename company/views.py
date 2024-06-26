from django.shortcuts import render

from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseForbidden
import uuid
from django.conf import settings
from django.core.mail import send_mail
from user.views import *

def company_register(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        email=request.POST.get('email')
        company_name = request.POST.get('company_name')
        logo = request.FILES.get('logo')
        description = request.POST.get('description')
        location = request.POST.get('location')
        phone_number = request.POST.get('phone_number')
        website = request.POST.get('website')
        industry = request.POST.get('industry')

        if password1==password2:

            user =CustomUser.objects.create_user(
                username=username,
                password=password1,
                email=email,
                role=2, 
            )
            CompanyProfile.objects.create(
                fk_company=user,
                company_name=company_name,
                logo=logo,
                description=description,
                location=location,
                phone_number=phone_number,
                website=website,
                industry=industry,
                company_status=False, #change
            )
            auth_token = str(uuid.uuid4())
            company_obj = CompanyAuth.objects.create(fk_company_auth = user, auth_token = auth_token)
            company_obj.save()
            send_mail_after_registration(email,auth_token)
            return redirect('token_send')

        else:
            messages.error(request,'incorrect password')
    return render(request,'company/company_register.html')



def company_home(request):
    company_profile=CompanyProfile.objects.filter(fk_company=request.user)
    company =CompanyProfile.objects.get(fk_company=request.user)
    if not company.company_status:          
         return HttpResponseForbidden("Your account is not yet approved by the admin.")  #change
    return render(request,'company/company_home.html',{'company':company,'company_profile':company_profile})

def company_profile(request):
    company = CompanyProfile.objects.get(fk_company=request.user)
    company_profile=CompanyProfile.objects.filter(fk_company=request.user)
    return render(request,'company/company_profile.html',{'company':company,'company_profile':company_profile})


def company_profile_edit(request,id):
    company=CompanyProfile.objects.get(id=id)
    if request.method == 'POST':
        logo = request.FILES.get('logo')
        description = request.POST.get('description')
        location = request.POST.get('location')
        phone_number = request.POST.get('phone_number')
        website = request.POST.get('website')
        industry = request.POST.get('industry')
        if logo:
            company.logo = logo
        if description:
            company.description = description
        if location:
            company.location = location
        if phone_number:
            company.phone_number = phone_number
        if website:
            company.website = website
        if industry:
            company.industry = industry
        company.save()
        return redirect('company_profile')
    return render(request,'company/company_profile_edit.html',{'company':company})

def company_job(request):
    company_profile=CompanyProfile.objects.filter(fk_company=request.user)
    company =CompanyProfile.objects.get(fk_company=request.user)
    company_joblist = JobAdd.objects.filter(fk_company_pro__fk_company=request.user)
    return render(request,'company/company_job.html',{'company':company,
                                                      'company_profile':company_profile,
                                                      'company_joblist':company_joblist})



def company_jobadd(request):
    company_profile=CompanyProfile.objects.filter(fk_company=request.user)
    company =CompanyProfile.objects.get(fk_company=request.user)
    if request.method == 'POST':
        job_title =request.POST.get('job_title')
        job_description =request.POST.get('job_description')
        job_type = request.POST.get('job_type')
        industry = request.POST.get('industry')
        location = request.POST.get('location')
        job_fields=request.POST.get('job_fields')
        salary = request.POST.get('salary')
        education_requirements = request.POST.get('education_requirements')
        experience_requirements = request.POST.get('experience_requirements')
        skills_and_qualifications = request.POST.get('skills_and_qualifications')
        application_deadline = request.POST.get('application_deadline')
        vacancy=request.POST.get('vacancy')
        JobAdd.objects.create(
            fk_company_pro=company,
            job_title=job_title,
            job_description=job_description,
            job_type=job_type,
            industry=industry,
            location=location,
            job_fields=job_fields,
            salary=salary,
            education_requirements=education_requirements,
            experience_requirements=experience_requirements,
            skills_and_qualifications=skills_and_qualifications,
            application_deadline=application_deadline,
            filled=False,
            vacancy=vacancy,
        )
        return redirect('company_job')
    return render(request,'company/company_jobadd.html',{'company':company,'company_profile':company_profile})




def checkfill(request,id):
    job = JobAdd.objects.get(id=id)
    if job:
        job.filled = not job.filled
        job.save()
    return redirect('company_job')


def company_jobedit(request, id):
    job = JobAdd.objects.get(id=id)
    
    if request.method == 'POST':
        job_title = request.POST.get('job_title')
        job_description = request.POST.get('job_description')
        job_type = request.POST.get('job_type')
        industry = request.POST.get('industry')
        location = request.POST.get('location')
        job_fields = request.POST.get('job_fields')
        salary = request.POST.get('salary')
        education_requirements = request.POST.get('education_requirements')
        experience_requirements = request.POST.get('experience_requirements')
        skills_and_qualifications = request.POST.get('skills_and_qualifications')
        application_deadline = request.POST.get('application_deadline')
        vacancy = request.POST.get('vacancy')
        
        # Example of conditional updates
        if job_title:
            job.job_title = job_title
        if job_description:
            job.job_description = job_description
        if job_type:
            job.job_type = job_type
        if industry:
            job.industry = industry
        if location:
            job.location = location
        if job_fields:
            job.job_fields = job_fields
        if salary:
            job.salary = salary
        if education_requirements:
            job.education_requirements = education_requirements
        if experience_requirements:
            job.experience_requirements = experience_requirements
        if skills_and_qualifications:
            job.skills_and_qualifications = skills_and_qualifications
        if application_deadline:
            job.application_deadline = application_deadline
        if vacancy:
            job.vacancy = vacancy

        job.save()
        
        return redirect('company_job')
    return render(request, 'company/company_jobedit.html', {'job': job})


def job_applicants(request):
    user=request.user
    all_appicants=Application.objects.filter(fk_company_job__fk_company_pro__fk_company=user)
    return render (request,'company/applicants_list.html',{'all_appicants':all_appicants})

def job_applicants_delete(request,id):
    all_appicants=Application.objects.filter(id=id)
    all_appicants.delete()
    return redirect('job_applicants')   

def change_applicant_status(request,id):
    change_status=Application.objects.get(id=id)
    if request.method == 'POST':
        s=request.POST.get('status')
        change_status.status=s
        change_status.save()
        return redirect('job_applicants')
    return render(request,'company/applicants_list.html',{'change':change_status})