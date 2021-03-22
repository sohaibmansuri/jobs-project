from django.db import models
# Create your models here.
class hydjobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=1000)
    title=models.CharField(max_length=1000)
    eligibility=models.CharField(max_length=1000)
    address=models.CharField(max_length=1000)
    email=models.EmailField()
    phonenumber=models.IntegerField()

class jprjobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=1000)
    title=models.CharField(max_length=1000)
    eligibility=models.CharField(max_length=1000)
    address=models.CharField(max_length=1000)
    email=models.EmailField()
    phonenumber=models.IntegerField()

class banglorejobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=1000)
    title=models.CharField(max_length=1000)
    eligibility=models.CharField(max_length=1000)
    address=models.CharField(max_length=1000)
    email=models.EmailField()
    phonenumber=models.IntegerField()

class delhijobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=1000)
    title=models.CharField(max_length=1000)
    eligibility=models.CharField(max_length=1000)
    address=models.CharField(max_length=1000)
    email=models.EmailField()
    phonenumber=models.IntegerField()
