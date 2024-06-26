from django.urls import path
from .views import *
from company.views import *


urlpatterns = [

    path('',home,name="home"),
    path('verify/<auth_token>',verify,name="verify"),
    path('all_login/',all_login,name='all_login'),
    path('error/',error,name='error'),
    path('success/',success,name='success'),
    path('token_send/',token_send,name='token_send'),

    path('applicant_register/',applicant_register,name='applicant_register'),  
    path('user_home/',user_home,name='user_home'),
    path('user_profile/',User_profile,name='user_profile'),
    path('edit_profile/<int:id>/',edit_profile, name='edit_profile'),
    path('logoutall/',logoutall,name='logoutall'),
    # urls.py
    
    path('edit_careerobj/<int:id>/',edit_careerobj, name='edit_careerobj'), 

    path('applicant_projects',applicant_projects,name='applicant_projects'), 
    path('applicant_projects_list',applicant_projects_list,name='applicant_projects_list'),
    path('edit_project/<int:id>/',edit_project, name='edit_project'), 

    path('applicant_keyskills',applicant_keyskills,name='applicant_keyskills'), 
    path('applicant_skills_list',applicant_skills_list,name='applicant_skills_list'), 
    path('edit_skills/<int:id>/',edit_keyskills, name='edit_skills'), 
    path('delete_keyskills/<int:id>/',delete_keyskills, name='delete_keyskills'), 

    path('create_education',create_education,name='create_education'), 
    path('list_education',list_education,name='list_education'), 
    path('edit_education/<int:id>/',edit_education, name='edit_education'), 
    path('delete_education/<int:id>/',delete_education, name='delete_education'), 

    path('create_experience',create_experience,name='create_experience'), 
    path('list_experience',list_experience,name='list_experience'), 
    path('edit_experience/<int:id>/',edit_experience, name='edit_experience'), 
    path('delete_experience/<int:id>/',delete_experience, name='delete_experience'), 

    path('create_languages',create_languages,name='create_languages'), 
    path('list_languages',list_languages,name='list_languages'), 
    path('edit_languages/<int:id>/',edit_languages, name='edit_languages'), 
    path('delete_languages/<int:id>/',delete_languages, name='delete_languages'), 

    path('job_list',job_list,name='job_list'),

    path('apply/<int:id>/',apply,name='apply'),






]