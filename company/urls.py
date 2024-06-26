from django.urls import path
from .views import *
from user.views import *



urlpatterns = [

    path('company_register',company_register,name="company_register"),
    path('company_home',company_home,name="company_home"),
    path('company_profile/',company_profile,name='company_profile'),
    path('company_profile_edit/<int:id>/',company_profile_edit, name='company_profile_edit'),

    path('company_job/',company_job,name='company_job'),
    path('company_jobadd/',company_jobadd,name='company_jobadd'),      
    path('filled/<int:id>/',checkfill,name='filled'),
    path('company_jobedit/<int:id>/',company_jobedit,name='company_jobedit')
    , 
    path('job_applicants/',job_applicants,name='job_applicants'),
    path('job_applicants_delete/<int:id>/',job_applicants_delete,name='job_applicants_delete'),
     path('change_applicant_status/<int:id>/',change_applicant_status,name='change_applicant_status'),
]