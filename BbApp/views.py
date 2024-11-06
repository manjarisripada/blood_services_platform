from django.shortcuts import render,redirect,HttpResponse
from datetime import date, timedelta
from .forms import userForm,AdForm,Uspform,DonorForm,StaffForm,MedicalForm,Requests,UpreqForm,Donors,UpDonorForm,ChgPwdForm,BloodStockForm
from django.contrib import messages
from .models import User,Donorpfl,Staffpfl,Med_per,Bloodrequests,Donate,BloodStock
# Create your views here.
def home(request):
    return render(request,'html/home.html')
def bloodgroups(request):
    stocks = BloodStock.objects.all()
    if request.method == "POST":
        f = BloodStockForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('/blgr')
    fo=BloodStockForm()
    return render(request,'html/bloodgroups.html',{'s':stocks,'p':fo})
def donat(request):
    k = Donate.objects.all()
    return render(request,'html/donations.html',{'t':k})
def requestss(request):
    k = Bloodrequests.objects.all()
    return render(request,'html/requests.html',{'t':k})
def register(request):
    if request.method == "POST":
        f = userForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request,"User Created Successfully")
            return redirect('/lgn')
    else:
        f = userForm()
        return render(request,'html/register.html',{'g':f}) 
def about(request):
    return render(request,'html/about.html')
def userlist(request):
    c= User.objects.all()
    n,m={},{}
    if request.method == "POST":
        s= AdForm(request.POST)
        if s.is_valid():
            s.save()
            messages.success(request,"User created successfully")
            return redirect('/usrlist')
        else:
            n[s] = s.errors
    for j in n.values():
        for v in j.items():
            m[v[0]] = v[1]
    s= AdForm()
    return render(request,'html/userlist.html',{'w':s,'p':m.items(),'k':c})
def profile(request):
    return render(request,'html/profile.html')
def updprofile(request):
    k=User.objects.get(id=request.user.id)
    if request.user.role_type == "1":
        t=Donorpfl.objects.all()
        m=[]
        for i in t:
            m.append(i.do_id)
        if request.user.id not in m:
            if request.method == "POST":
                h=Uspform(request.POST,request.FILES,instance=k)  
                y=DonorForm(request.POST) 
                if h.is_valid() and y.is_valid():
                    h.save()
                    b=y.save(commit=False)
                    b.do_id=request.user.id
                    b.dstatus=1
                    b.save()
                    return redirect('/pfle')
            y=DonorForm()
            h=Uspform(instance=k)
            return render(request,'html/updateprofile.html',{'e':h,'t':y})
        else:
            p=Donorpfl.objects.get(do_id=request.user.id)
            if request.method == "POST":
                h=Uspform(request.POST,request.FILES,instance=k)  
                y=DonorForm(request.POST,instance=p) 
                if h.is_valid() and y.is_valid():
                    h.save()
                    y.save()
                    return redirect('/pfle')
            y=DonorForm(instance=p)
            h=Uspform(instance=k)
            return render(request,'html/updateprofile.html',{'e':h,'t':y})
    elif request.user.role_type == "2":
        t=Staffpfl.objects.all()
        m=[]
        for i in t:
            m.append(i.st_id)
        if request.user.id not in m:
            if request.method == "POST":
                h=Uspform(request.POST,request.FILES,instance=k)  
                y=StaffForm(request.POST) 
                if h.is_valid() and y.is_valid():
                    h.save()
                    b=y.save(commit=False)
                    b.st_id=request.user.id
                    b.sstatus=1
                    b.save()
                    return redirect('/pfle')
            y=StaffForm()
            h=Uspform(instance=k)
            return render(request,'html/updateprofile.html',{'e':h,'t':y})
        else:
            p=Staffpfl.objects.get(st_id=request.user.id)
            if request.method == "POST":
                h=Uspform(request.POST,request.FILES,instance=k)  
                y=StaffForm(request.POST,instance=p) 
                if h.is_valid() and y.is_valid():
                    h.save()
                    y.save()
                    return redirect('/pfle')
            y=StaffForm(instance=p)
            h=Uspform(instance=k)
            return render(request,'html/updateprofile.html',{'e':h,'t':y})
    elif request.user.role_type == "3":
        t=Med_per.objects.all()
        m=[]
        for i in t:
            m.append(i.md_id)
        if request.user.id not in m:
            if request.method == "POST":
                h=Uspform(request.POST,request.FILES,instance=k)  
                y=MedicalForm(request.POST) 
                if h.is_valid() and y.is_valid():
                    h.save()
                    b=y.save(commit=False)
                    b.md_id=request.user.id
                    b.mstatus=1
                    b.save()
                    return redirect('/pfle')
            y=MedicalForm()
            h=Uspform(instance=k)
            return render(request,'html/updateprofile.html',{'e':h,'t':y})
        else:
            p=Med_per.objects.get(md_id=request.user.id)
            if request.method == "POST":
                h=Uspform(request.POST,request.FILES,instance=k)  
                y=MedicalForm(request.POST,instance=p) 
                if h.is_valid() and y.is_valid():
                    h.save()
                    y.save()
                    return redirect('/pfle')
            y=MedicalForm(instance=p)
            h=Uspform(instance=k)
            return render(request,'html/updateprofile.html',{'e':h,'t':y})
    else:
        if request.method == "POST":
            h=Uspform(request.POST,request.FILES,instance=k)   
            if h.is_valid():
                h.save()
                return redirect('/pfle')
        h=Uspform(instance=k)
        return render(request,'html/updateprofile.html',{'e':h})

def requestmain(request):
    p = Bloodrequests.objects.filter(re_id = request.user.id)
    if request.method == "POST":
        d=Requests(request.POST)
        if d.is_valid():
            w=d.save(commit=False)
            w.re_id=request.user.id
            w.save()
            return redirect('/reqm')
    d=Requests()
    return render(request,'html/reqmain.html',{'z':d,'h':p})
def uprequest(request,w):
    b = Bloodrequests.objects.get(id=w)
    if request.method == "POST":
        g = UpreqForm(request.POST,instance=b)
        if g.is_valid():
            g.save()
            if b.status == 'a':
                blood_group = b.bloodgroup
                units_requested = b.unit
                stock = BloodStock.objects.get(blood_group=blood_group)
                stock.units -= units_requested
                stock.save()
            return redirect('/reqa')
    g = UpreqForm(instance=b)
    return render(request,'html/updaterequest.html',{'t':g})
def reqdlt(request,p):
    k = Bloodrequests.objects.get(id=p)
    if request.method == "POST":
        k.delete()
        return redirect('/reqa')
    return render(request,'html/delreq.html',{'a':k})
def donatee(request):
    p = Donate.objects.filter(don_id = request.user.id)
    n=Donate.objects.filter(don_id = request.user.id).order_by('-apldate').first()
    today = date.today()
    three_months_ago = today - timedelta(days=90)
    if n and n.apldate > three_months_ago:
        return HttpResponse("You can donate again after 3 months.")
    if request.method == "POST":
        d=Donors(request.POST)
        if d.is_valid():
            w=d.save(commit=False)
            w.don_id=request.user.id
            w.save()
            blood_group = w.blood_group
            units_donated = w.units
            stock = BloodStock.objects.get(blood_group=blood_group)
            stock.units += units_donated
            stock.save()
            return redirect('/lgn')
    d=Donors()
    return render(request,'html/donor_donate.html',{'z':d,'h':p})
def updonate(request,w):
    b = Donate.objects.get(id=w)
    if request.method == "POST":
        g = UpDonorForm(request.POST,instance=b)
        if g.is_valid():
            g.save()
            return redirect('/dodo')
    g = UpDonorForm(instance=b)
    return render(request,'html/updatedonar.html',{'t':g})
def dondlt(request,p):
    k = Donate.objects.get(id=p)
    if request.method == "POST":
        k.delete()
        return redirect('/dodo')
    return render(request,'html/deldona.html',{'a':k})
def chgepwd(request):
	if request.method == "POST":
		n = ChgPwdForm(user=request.user,data=request.POST)
		if n.is_valid():
			n.save()
			return redirect('/lgn')
	n = ChgPwdForm(user=request)
	return render(request,'html/changepaswd.html',{'h':n})
def userdlt(request,p):
    k = User.objects.get(id=p)
    if request.method == "POST":
        k.delete()
        return redirect('/usrlist')
    return render(request,'html/deluser.html',{'a':k})

