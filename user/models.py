from django.db import models
from my_admin_app.models import *
# Applicant Details
class ApplicantProfile(models.Model):

    GENDER_CHOICES = [
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('OTHERS', 'Others'),
    ]

    MARITAL_STATUS_CHOICES = [
        ('SINGLE', 'Single'),
        ('MARRIED', 'Married'),
        ('DIVORCED', 'Divorced'),
        ('WIDOWED', 'Widowed'),
    ]

    WORK_STATUS_CHOICES = [
        ('Experienced', 'I have work experience'),
        ('Fresher', 'I am a fresher'),
    ]

    fk_user=models.OneToOneField(CustomUser,on_delete=models.CASCADE) 
    photo=models.ImageField(upload_to='Profile_Photo/')
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    gender=models.CharField( max_length=50,choices=GENDER_CHOICES)
    marital_status=models.CharField(max_length=50,choices=MARITAL_STATUS_CHOICES)
    dob=models.DateField()
    address=models.TextField()
    phone=models.CharField(max_length=12)
    workstatus=models.CharField(max_length=100,choices=WORK_STATUS_CHOICES)
    jobrole=models.CharField(max_length=100)


class Resume(models.Model):
    fk_user=models.OneToOneField(CustomUser,on_delete=models.CASCADE) 
    resume=models.FileField(upload_to='Resume/')

class Projects(models.Model):
    fk_user=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    project_name=models.CharField(max_length=100)
    project_description=models.TextField()
    project_link=models.URLField()

class CareerObj(models.Model):
    fk_user=models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    career_obj=models.TextField()



class Education(models.Model):
    LEVEL_CHOICES = (
        ('HighSchool', 'High School'),
        ('HigherSecondarySchool', 'Higher Secondary'),
        ('Graduation/Diploma', 'Graduation/Diploma'),
        ('PostGraduation', 'Post Graduation'),
        ('PhD', 'PhD'),
    )
    fk_user=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    level = models.CharField(max_length=100, choices=LEVEL_CHOICES)
    school_or_university = models.CharField(max_length=200)
    course = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    additional_details = models.TextField()


class ApplicantAuth(models.Model):
    fk_user_auth=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100)
    is_verified=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fk_user_auth.username


class KeySkills(models.Model):
    fk_user=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    key_skills=models.CharField(max_length=100)

class Languages(models.Model):
    PROFICIENCY=(
        ('BEGINNER','BEGINNER'),
        ('PROFICIENT','PROFICIENT'),
        ('EXPERT','EXPERT'),
    )
    fk_user=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    languages=models.CharField(max_length=100)
    proficiency=models.CharField(max_length=100,choices=PROFICIENCY)
    read=models.BooleanField(default=False,null=True)
    write=models.BooleanField(default=False,null=True)
    speak=models.BooleanField(default=False,null=True)


class Experience(models.Model):
    PERIOD=(
        ('15_Days_and_less','15_Days_and_less'),
        ('1Month','1Month'),
        ('2Month','2Month'),
        ('3Month','3Month'),
        ('MoreThan3Month','MoreThan3Month'),
        ('ServingNoticePeriod','ServingNoticePeriod'),
    )
    fk_user=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    is_this_current_emp=models.BooleanField(default=False,null=True)
    current_company_name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    doj=models.DateField()
    current_salary=models.PositiveIntegerField()
    job_profile=models.TextField()
    notice_period=models.CharField(max_length=50,choices=PERIOD)
    dol=models.DateField()
