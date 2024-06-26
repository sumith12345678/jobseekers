from django.contrib import admin
from .models import *


class CustomApplicant(admin.ModelAdmin):
    list_display = ('id','fk_user','firstname','lastname','gender','dob','phone','address','workstatus')

class CustomEducation(admin.ModelAdmin):
    list_display=('id','fk_user','level','school_or_university','course')

class CustomCompany(admin.ModelAdmin):
    list_display=('id','fk_company','company_name','logo','description','location','phone_number','website','industry')

class CustomExperience(admin.ModelAdmin):
    list_display=('id','fk_user','current_company_name','location','doj','dol','current_salary','notice_period')

class CustomKeyskills(admin.ModelAdmin):
    list_display=('id','fk_user','key_skills')

class CustomLanguages(admin.ModelAdmin):
    list_display=('id','fk_user','languages','proficiency')

class CustomJobadd(admin.ModelAdmin):
    list_display=('id','fk_company_pro','job_title','job_type','industry','location','job_fields','vacancy','salary','education_requirements','experience_requirements')

class CustomApplication(admin.ModelAdmin):
    list_display=('id','fk_user_pro','fk_company_job',)

class CustomResume(admin.ModelAdmin):
    list_display=('id','fk_user','resume')

class CustomProjects(admin.ModelAdmin):
    list_display=('id','fk_user','project_name','project_description','project_link')

class CustomCareerObj(admin.ModelAdmin):
    list_display=('id','fk_user','career_obj')

class CustomKeyskills(admin.ModelAdmin):
    list_display=('id','fk_user','key_skills')

class CustomEducation(admin.ModelAdmin):
    list_display=('id','fk_user','level','school_or_university','course')

class CustomExperience(admin.ModelAdmin):
    list_display=('id','fk_user','current_company_name','location','doj','dol','current_salary','notice_period')

class CustomLanguages(admin.ModelAdmin):
    list_display=('id','fk_user','languages','proficiency','read','write','speak')
    
class CustomUserAuth(admin.ModelAdmin):
    list_display=('id','fk_user_auth','auth_token','is_verified','created_at')


admin.site.register(ApplicantProfile,CustomApplicant)
admin.site.register(Education,CustomEducation)
admin.site.register(CareerObj,CustomCareerObj)
admin.site.register(Resume,CustomResume)
admin.site.register(Projects,CustomProjects)
admin.site.register(ApplicantAuth,CustomUserAuth)
admin.site.register(KeySkills,CustomKeyskills)
admin.site.register(Experience,CustomExperience)
admin.site.register(Languages,CustomLanguages)
