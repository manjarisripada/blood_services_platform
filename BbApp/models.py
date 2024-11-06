from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser,Group,Permission


# Create your models here.
class User(AbstractUser):
    g=[
        ('0','--- Select your Gender ---'),
        ('1',"Male"),
        ('2','Female'),
    ]
    b=[
        ('0','Guest'),
        ('1','Donor'),
        ('2','Staff'),
        ('3','med_per'),
    ]
    mble=models.CharField(max_length=10,null=True,blank=True)
    gdr=models.CharField(choices=g,default='0',max_length=10)
    role_type=models.CharField(choices=b,default='0',max_length=10)
    pfimg=models.ImageField(upload_to='Profiles/',default='pfle.png')

class Donorpfl(models.Model):
    bloodgroup = models.CharField(max_length=10)
    address = models.CharField(max_length=40)
    dstatus = models.BooleanField(default=False)
    do = models.OneToOneField(User, on_delete=models.CASCADE)

class Staffpfl(models.Model):
    s_num = models.CharField(max_length=10)
    quali = models.CharField(max_length=40)
    sstatus = models.BooleanField(default=False)
    st = models.OneToOneField(User, on_delete=models.CASCADE)

class Med_per(models.Model):
    M_num = models.CharField(max_length=10)
    quali = models.CharField(max_length=40)
    Med_Li_Num = models.CharField(max_length=20)
    mstatus = models.BooleanField(default=False)
    md = models.OneToOneField(User, on_delete=models.CASCADE)

class Bloodrequests(models.Model):
    d = [
		('g','Pending'),
		('a','Approved'),
		('d','Declined'),
	]
    patient_name=models.CharField(max_length=20)
    patient_age=models.IntegerField()
    bloodgroup=models.CharField(max_length=10)
    unit=models.IntegerField(default=0)
    apldate = models.DateField(auto_now_add=True)
    disease=models.CharField(max_length=100)
    status = models.CharField(choices=d,default='g',max_length=10)
    Med_perdesc = models.CharField(max_length=200,blank=False)
    re = models.ForeignKey(User,on_delete=models.CASCADE)
class Donate(models.Model):
    d = [
		('g','Pending'),
		('a','Approved'),
		('d','Declined'),
	]
    donor_name=models.CharField(max_length=20)
    donor_age=models.IntegerField()
    blood_group=models.CharField(max_length=10)
    units=models.IntegerField(default=0)
    apldate = models.DateField(auto_now_add=True)
    diseases=models.CharField(max_length=100)
    status = models.CharField(choices=d,default='g',max_length=10)
    Med_perdesc = models.CharField(max_length=200,blank=False)
    don = models.ForeignKey(User,on_delete=models.CASCADE)

class BloodStock(models.Model):
    blood_group = models.CharField(max_length=5, unique=True)
    units = models.PositiveIntegerField(default=0)


