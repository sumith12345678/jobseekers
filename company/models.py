from django.db import models
from my_admin_app.models import *
from user.models import *
from django.utils import timezone

# Create your models here.

class CompanyAuth(models.Model):
    fk_company_auth=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100)
    is_verified=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fk_company_auth.username

class CompanyProfile(models.Model):
    fk_company=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='Company_Logos/')
    description = models.TextField(null=True)
    location = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    website = models.URLField()
    industry = models.CharField(max_length=100)
    company_status=models.BooleanField(default=False) #change



class JobAdd(models.Model):
    JOBTYPE=(
        ('Full_Time','Fulltime'),
        ('Part_time','Part_time'),
        ('Contract','Contract'),
        ('Internship','Internship'),
    )
    fk_company_pro=models.ForeignKey(CompanyProfile, on_delete=models.CASCADE) #companyprofile FK_company
    job_title = models.CharField(max_length=200)
    job_description = models.TextField()
    job_type = models.CharField(max_length=100,choices=JOBTYPE)
    industry = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    job_fields=models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    education_requirements = models.CharField(max_length=100)
    experience_requirements = models.CharField(max_length=100)
    skills_and_qualifications = models.TextField()
    application_deadline = models.DateTimeField()
    filled=models.BooleanField(default=False)
    vacancy=models.IntegerField(default=1)
    date_posted = models.DateTimeField(auto_now_add=True)
    time_posted = models.TimeField(auto_now_add=True) 
    updated_date=models.DateField(auto_now=True)

    def __str__(self):
        return self.fk_company_pro.company_name


class Application(models.Model):
    fk_user_pro=models.ForeignKey(ApplicantProfile, on_delete=models.CASCADE)# employee
    fk_company_job=models.ForeignKey(JobAdd, on_delete=models.CASCADE)# employer
    resume=models.FileField(upload_to='latest_Resume/',null=True)
    status=models.CharField(max_length=20,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
