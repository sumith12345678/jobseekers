from django.urls import path
from .views import *


urlpatterns = [

    path('',admin_home,name="admin_home"),

    path('admin_company_list',admin_company_list,name="admin_company_list"),
    path('admin_approve_company/<int:id>/',admin_approve_company,name='admin_approve_company'),
    path('admin_company_view/<int:id>/',admin_company_view,name='admin_company_view'),
    path('admin_company_delete/<int:id>/',admin_company_delete,name='admin_company_delete'),

    path('admin_user_list',admin_user_list,name="admin_user_list"),
    path('admin_user_view/<int:id>/',admin_user_view,name='admin_user_view'),
    path('admin_user_delete/<int:id>/',admin_user_delete,name='admin_user_delete'),
]