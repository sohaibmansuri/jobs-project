from django.contrib import admin
from testApp.models import hydjobs,jprjobs,banglorejobs,delhijobs
# Register your models here.
class hyd_info(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']

class jpr_info(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']

class banglore_info(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']

class delhi_info(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']

admin.site.register(hydjobs,hyd_info)
admin.site.register(jprjobs,jpr_info)
admin.site.register(banglorejobs,banglore_info)
admin.site.register(delhijobs,delhi_info)
