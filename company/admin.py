from django.contrib import admin
from .models import *
# Register your models here.


class CustomCompanyAuth(admin.ModelAdmin):
    list_display=('id','fk_company_auth','auth_token','is_verified','created_at')

class CustomJobadd(admin.ModelAdmin):
    list_display=('id','fk_company_pro','job_title','job_type','filled','industry',
                  'location','job_fields','vacancy','salary','education_requirements',
                  'experience_requirements','date_posted','updated_date','time_posted')


class CustomCompany(admin.ModelAdmin):
    list_display=('id','fk_company','company_name','logo','description','location','phone_number','website','industry','company_status')


class CustomApplication(admin.ModelAdmin):
    list_display=('id','fk_user_pro','fk_company_job','resume','status','created_at')



admin.site.register(JobAdd,CustomJobadd)
admin.site.register(CompanyAuth,CustomCompanyAuth)
admin.site.register(CompanyProfile,CustomCompany)
admin.site.register(Application,CustomApplication)



