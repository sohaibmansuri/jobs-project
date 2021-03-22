
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','jobsProject.settings')
import django
django.setup()

from testApp.models import *
from faker import Faker
from random import *
fake=Faker()

def phonenumbergen():
    d1=randint(7,9)
    num='' + str(d1)
    for x in range(9):
        num=num+str(randint(0,9))
    return int(num)
def populate(n):
    for x in range(n):
        fdate=fake.date()
        fcompany=fake.company()
        ftitle=fake.random_element(elements=('Project Manager','Team Leader','Software Engineer'))
        feligibility=fake.random_element(elements=('M.tech','B.tech','Phd'))
        faddress=fake.address()
        femail=fake.email()
        fnumber=phonenumbergen()
        hyd_records=hydjobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligibility,
        address=faddress,email=femail,phonenumber=fnumber)
populate(10)
