from django.shortcuts import render
from testApp.models import *
# Create your views here.
def home(request):
    return render(request,'testApp/home.html')

def jaipur(request):
    jpr_data=jprjobs.objects.order_by('date')
    jpr_jobs={'jpr_data':jpr_data}
    return render(request,'testApp/jpr.html',context=jpr_jobs)

def hyd(request):
    hyd_data=hydjobs.objects.all()
    hyd_jobs={'hyd_data':hyd_data}
    return render(request,'testApp/hyd.html',context=hyd_jobs)

def banglore(request):
    ban_data=banglorejobs.objects.order_by('date')
    ban_jobs={'ban_data':ban_data}
    return render(request,'testApp/banglore.html',context=ban_jobs)

def delhi(request):
    del_data=delhijobs.objects.order_by('date')
    del_jobs={'del_data':del_data}
    return render(request,'testApp/delhi.html',context=del_jobs)
