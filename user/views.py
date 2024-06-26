from django.shortcuts import render

# Create your views here.


def custom_404(request, exception):
    return render(request, 'user/404.html', {'exception': exception}, status=404)
    
def home(request):
    return render(request, 'user/home.html')






from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseForbidden
import uuid
from django.conf import settings
from django.core.mail import send_mail
from company.models import *
# from django.contrib.auth.decorators import login_required





#APPLICANT

def applicant_register(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        email=request.POST.get('email')
        if password1==password2:
            user=CustomUser.objects.create_user(
                username=username,
                password=password1,
                email=email,
                role=3, 
            )
            auth_token = str(uuid.uuid4())
            applicant_obj = ApplicantAuth.objects.create(fk_user_auth = user , auth_token = auth_token)
            applicant_obj.save()
            send_mail_after_registration(email,auth_token)
            return redirect('token_send')
            # return redirect ('all_login')
        else:
            messages.error(request,'incorrect password')
    return render(request,'user/register.html')


def token_send(request):
    return render(request,'base/token_send.html')

def send_mail_after_registration(email , token):
    subject = 'Your accounts need to be verified'
    message = f'Hi paste the link to verify your account http://127.0.0.1:8000/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    print(email)
    print(token)
    send_mail(subject, message , email_from ,recipient_list )


# Verify Account
def verify(request, auth_token):
    try:
        applicant_obj = ApplicantAuth.objects.filter(auth_token=auth_token).first()
        if applicant_obj:
            if applicant_obj.is_verified:
                messages.success(request, 'Your account is already verified.')
                return redirect('all_login')
            applicant_obj.is_verified = True
            applicant_obj.save()
            messages.success(request, 'Your account has been verified.')
            return redirect('success')
        
        company_obj = CompanyAuth.objects.filter(auth_token=auth_token).first()
        if company_obj:
            if company_obj.is_verified:
                messages.success(request, 'Your account is already verified.')
                return redirect('all_login')
            company_obj.is_verified = True
            company_obj.save()
            messages.success(request, 'Your account has been verified.')
            return redirect('success')
        else:
            messages.error(request, 'Invalid token')
            return redirect('error')
    except Exception as e:
        print(e)
        return redirect('error')

    
def error(request):
    return render (request,'base/error.html')

def success(request):
    return render(request,'base/success.html')


def all_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.role == 1:
                request.session['user'] = user.username
                login(request, user)
                return redirect('admin_home')

            applicant_auth = ApplicantAuth.objects.filter(fk_user_auth=user).first()
            company_auth = CompanyAuth.objects.filter(fk_company_auth=user).first()

            if user.role == 3 and applicant_auth and applicant_auth.is_verified:
                request.session['user'] = user.username
                login(request, user)
                return redirect('user_home')

            elif user.role == 2 and company_auth and company_auth.is_verified:
                # company_profile = CompanyProfile.objects.filter(fk_company=user).first()
                # if company_profile and company_profile.company_status:  # Check if company_status is True
                    request.session['user'] = user.username
                    login(request, user)
                    return redirect('company_home')
           

            else:
                messages.error(request, 'Your account is not verified. Please check your email for the verification link.')
                return redirect('all_login')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('all_login')

    return render(request, 'base/login.html')


def logoutall(request):
    logout(request)
    return redirect ('all_login')


def user_home(request):
    user=request.user
    user_profile=ApplicantProfile.objects.filter(fk_user=user)
    user_career=CareerObj.objects.filter(fk_user=user)
    user_proj=Projects.objects.filter(fk_user=user)
    user_skills =KeySkills.objects.filter(fk_user=user)
    user_education =Education.objects.filter(fk_user=user)
    user_experience =Experience.objects.filter(fk_user=user)
    user_language = Languages.objects.filter(fk_user=user)
    return render (request,'user/user_home.html',
                   {'user':user,'user_profile':user_profile,
                    'user_career':user_career,'user_proj':user_proj,
                    'user_skills':user_skills,'user_education':user_education,
                    'user_experience':user_experience,'user_language':user_language})




def User_profile(request):
    if request.method == 'POST':
        user=request.user
        photo=request.FILES.get('photo')
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        gender=request.POST.get('gender')
        marital_status=request.POST.get('marital_status')
        dob=request.POST.get('dob')
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        workstatus=request.POST.get('workstatus')
        career_obj=request.POST.get('career_obj')
        resume=request.FILES.get('resume')
        jobrole=request.POST.get('jobrole')
    
        ApplicantProfile.objects.create(
                fk_user=user,
                photo=photo,
                firstname=firstname,
                lastname=lastname,
                gender=gender,
                marital_status=marital_status,
                dob=dob,
                address=address,
                phone=phone,
                workstatus=workstatus,
                jobrole=jobrole,
        )
        Resume.objects.create(
            fk_user=user,
            resume=resume,
        )
        CareerObj.objects.create(
            fk_user=user,
            career_obj=career_obj,
        )
        return redirect ('user_home')
    return render(request,'user/profile.html')

def edit_profile(request,id):
    profile=ApplicantProfile.objects.get(id=id)
    if request.method == 'POST':
        photo=request.FILES.get('photo')
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        gender=request.POST.get('gender')
        marital_status=request.POST.get('marital_status')
        dob=request.POST.get('dob')
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        workstatus=request.POST.get('workstatus')
        jobrole=request.POST.get('jobrole')
        
        if photo:
            profile.photo=photo
        if firstname:
            profile.firstname=firstname
        if lastname:
            profile.lastname=lastname
        if gender:
            profile.gender=gender
        if marital_status:
            profile.marital_status=marital_status
        if dob:
            profile.dob=dob
        if address:
            profile.address=address
        if phone:
            profile.phone=phone
        if workstatus:
            profile.workstatus=workstatus
        if jobrole:
            profile.jobrole=jobrole
        profile.save()
        return redirect ('user_home')
    return render (request,'user/editprofile.html',{'profile':profile})

def edit_careerobj(request,id):
    career=CareerObj.objects.get(id=id)
    if request.method == 'POST':
        career_obj=request.POST.get('career_obj')
        career.career_obj=career_obj
        career.save()
        return redirect ('user_home')
    return render(request,'user/editcareerobj.html',{'career':career})


def applicant_projects(request):
    if request.method == 'POST':
        user=request.user
        project_name=request.POST.get('project_name')
        project_description=request.POST.get('project_description')
        project_link=request.POST.get('project_link')
        Projects.objects.create(
            fk_user=user,
            project_name=project_name,
            project_description=project_description,
            project_link=project_link,
        )
        return redirect ('user_home')
    return render(request,'user/projects.html')


def applicant_projects_list(request):
    user = request.user
    user_projects = Projects.objects.filter(fk_user = user)
    
    context = {
        'user_projects': user_projects
    }
    return render(request, 'user/project_list.html', context)


def edit_project(request,id):
    proj=Projects.objects.get(id=id)
    if request.method == 'POST':
        project_name=request.POST.get('project_name')
        project_description=request.POST.get('project_description')
        project_link=request.POST.get('project_link')
        proj.project_name=project_name
        proj.project_description=project_description
        proj.project_link=project_link
        proj.save()
        return redirect ('user_home')
    return render(request,'user/editproject.html',{'proj':proj})

# skills  ###################################################

def applicant_keyskills(request):
    if request.method == 'POST':
        user=request.user
        key_skills=request.POST.get('key_skills')
        KeySkills.objects.create(
            fk_user=user,
            key_skills=key_skills,
        )
        return redirect ('applicant_skills_list')
    return render(request,'user/keyskills.html')

def applicant_skills_list(request):
    user = request.user
    user_skills = KeySkills.objects.filter(fk_user = user)
    
    context = {
        'user_skills': user_skills
    }
    return render(request, 'user/skills_list.html', context)

def edit_keyskills(request,id):
    skills=KeySkills.objects.get(id=id)
    if request.method == 'POST':
        skill=request.POST.get('key_skills')
        skills.key_skills=skill
        skills.save()
        return redirect ('applicant_skills_list')
    return render (request,'user/edit_keyskills.html',{'skills':skills})

def delete_keyskills(request, id):
    data = KeySkills.objects.filter(id=id)
    data.delete()
    return redirect('applicant_skills_list')


# Education   ###################################################

def create_education(request):
    if request.method == 'POST':
        user=request.user
        level = request.POST.get('level')
        school_or_university = request.POST.get('school_or_university')
        course = request.POST.get('course')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        additional_details = request.POST.get('additional_details')
        Education.objects.create(
            fk_user=user,
            level = level,
            school_or_university = school_or_university,
            course = course,
            start_date = start_date,
            end_date = end_date,
            additional_details = additional_details,
        )
        return redirect ('list_education')
    return render(request,'user/create_education.html')


def list_education(request):
    list_education=Education.objects.filter(fk_user=request.user)
    return render(request,'user/list_education.html',{'list_education':list_education})

def edit_education(request,id):
    education=Education.objects.get(id=id)
    if request.method == 'POST':
        level = request.POST.get('level')
        school_or_university = request.POST.get('school_or_university')
        course = request.POST.get('course')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        additional_details = request.POST.get('additional_details')
        education.level = level
        education.school_or_university = school_or_university
        education.course = course
        education.start_date = start_date
        education.end_date = end_date
        education.additional_details = additional_details
        education.save()
        return redirect ('list_education')
    return render (request,'user/edit_education.html',{'education':education})

def delete_education(request, id):
    data = Education.objects.filter(id=id)
    data.delete()
    return redirect('list_education')



# Experience ###################################################

def create_experience(request): 
    if request.method == 'POST':
        user=request.user
        is_this_current_emp=request.POST.get('is_this_current_emp') == 'on'
        current_company_name=request.POST.get('current_company_name')
        location=request.POST.get('location')
        doj=request.POST.get('doj')
        current_salary=request.POST.get('current_salary')
        job_profile=request.POST.get('job_profile')
        notice_period=request.POST.get('notice_period')
        dol=request.POST.get('dol')
        Experience.objects.create(
            fk_user=user,
            is_this_current_emp=is_this_current_emp,
            current_company_name=current_company_name,
            location=location,
            doj=doj,
            current_salary=current_salary,
            job_profile=job_profile,
            notice_period=notice_period,
            dol=dol,
        )
        return redirect ('list_experience')
    return render(request,'user/create_experience.html')


def list_experience(request):
    list_experience=Experience.objects.filter(fk_user=request.user)
    return render(request,'user/list_experience.html',{'list_experience':list_experience })

def edit_experience(request,id):
    experience=Experience.objects.get(id=id)
    if request.method == 'POST':
        current_company_name=request.POST.get('current_company_name')
        location=request.POST.get('location')
        doj=request.POST.get('doj')
        current_salary=request.POST.get('current_salary')
        job_profile=request.POST.get('job_profile')
        notice_period=request.POST.get('notice_period')
        dol=request.POST.get('dol')
        experience.current_company_name=current_company_name
        experience.location=location
        experience.doj=doj
        experience.current_salary=current_salary
        experience.job_profile=job_profile
        experience.notice_period=notice_period
        experience.dol=dol
        experience.save()
        return redirect ('list_experience')
    return render (request,'user/edit_experience.html',{'experience':experience})

def delete_experience(request, id):
    data = Experience.objects.filter(id=id)
    data.delete()
    return redirect('list_experience')


# Language ###################################################


def create_languages(request): 
   if request.method == 'POST':
        user=request.user
        languages =request.POST.get('languages')
        proficiency =request.POST.get('proficiency')
        read =request.POST.get('read') == 'on'
        write =request.POST.get('write') == 'on'
        speak = request.POST.get('speak') == 'on'
        Languages.objects.create(
            fk_user=user,
            languages=languages,
            proficiency=proficiency,
            read=read,
            write=write,
            speak=speak,
        )
        return redirect ('list_languages')
   return render(request,'user/create_languages.html')


def list_languages(request):
    list_languages=Languages.objects.filter(fk_user=request.user)
    return render(request,'user/list_languages.html',{'list_languages':list_languages })

def edit_languages(request,id):
    language=Languages.objects.get(id=id)
    if request.method == 'POST':
        languages =request.POST.get('languages')
        proficiency =request.POST.get('proficiency')
        read =request.POST.get('read') == 'on'
        write =request.POST.get('write') == 'on'
        speak = request.POST.get('speak') == 'on'
        language.languages=languages
        language.proficiency=proficiency
        language.read=read
        language.write=write
        language.speak=speak
        language.save()
        return redirect ('list_languages')
    return render (request,'user/edit_languages.html',{'language':language})

def delete_languages(request, id):
    data = Languages.objects.filter(id=id)
    data.delete()
    return redirect('list_languages')

############################ Job List #############################



from django.shortcuts import render
from company.models import JobAdd  # Adjust import path as per your actual project structure
from django.core.paginator import Paginator

def job_list(request):
    jobs = JobAdd.objects.filter(filled=False).order_by('-date_posted', '-updated_date')
    
    # Pagination
    paginator = Paginator(jobs, 6)  # Show 10 jobs per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'user/job_list.html', {'page_obj': page_obj})


def apply(request,id):
    user=ApplicantProfile.objects.get(fk_user=request.user)
    job=JobAdd.objects.get(id=id)
    application=Application.objects.filter(fk_user_pro=user,fk_company_job=job)
    if request.method == 'POST':
        resume=request.FILES.get('resume')
        Application.objects.create(
            fk_user_pro=user,
            fk_company_job=job,
            resume=resume,
            status='pending',
        )
        return redirect('job_list')
    return render(request,'user/apply_iob.html',{'job':job,'user':user ,'application':application})
