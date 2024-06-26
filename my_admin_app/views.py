from django.shortcuts import render,redirect
from .models import *
from company.models import *
from user.models import *
# Create your views here.

def admin_home(request):
    user = request.user
    user_count = ApplicantProfile.objects.count()
    company_approved = CompanyProfile.objects.filter(company_status=True).count()
    company_pending = CompanyProfile.objects.filter(company_status=False).count()
    total_members = CustomUser.objects.count()
    return render(request, 'admin/admin_home.html' ,{'user':user,'user_count':user_count,
                                                     'company_approved':company_approved,
                                                     'company_pending':company_pending,
                                                     'total_members':total_members})

def admin_company_list(request):
    company_list = CompanyProfile.objects.all().order_by('-id')
    return render(request, 'admin/admin_company_list.html',{'company_list':company_list})


def admin_approve_company(request,id):
    comp=CompanyProfile.objects.get(id=id)
    if comp:
        comp.company_status = not comp.company_status
        comp.save()
    return redirect('admin_company_list')

def admin_company_view(request,id):
    company=CompanyProfile.objects.filter(id=id)
    context={'company':company}
    return render(request,'admin/company_view.html',context)

def admin_company_delete(request,id):
    user=CustomUser.objects.filter(id=id)
    user.delete()
    return redirect('admin_company_list')

def admin_user_list(request):
    user_list = ApplicantProfile.objects.all().order_by('-id')
    return render(request, 'admin/admin_user_list.html',{'user_list':user_list})



def admin_user_view(request,id):
    applicants=ApplicantProfile.objects.filter(id=id)
    context={'applicants':applicants}
    return render(request,'admin/admin_user_view.html',context)

def admin_user_delete(request,id):
    user=CustomUser.objects.filter(id=id)
    user.delete()
    return redirect('admin_user_list')