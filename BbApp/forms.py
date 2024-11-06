from .models import User,Donorpfl,Staffpfl,Med_per,Bloodrequests,Donate,BloodStock
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django import forms

class userForm(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Password"}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Password Again"}))
	class Meta:
		model = User
		fields = ["username"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Username",
			}),
		}
class AdForm(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Password"}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Password Again"}))
	class Meta:
		model= User
		fields = ["username","role_type"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Username",
			}),
		"role_type":forms.Select(attrs={
			"class":"form-control my-2",
        }),
		}

class Uspform(forms.ModelForm):
	class Meta:
		model=User
		fields=["username","first_name","last_name","email","mble","gdr","pfimg"]
		widgets = {
			"username":forms.TextInput(attrs={
				"class":"form-control my-2",
				"readonly":"true",
			}),
			"first_name":forms.TextInput(attrs={
				"class":"form-control my-2",
				"placeholder":"First Name",
			}),
			"last_name":forms.TextInput(attrs={
				"class":"form-control my-2",
				"placeholder":"Last Name",
			}),
			"email":forms.EmailInput(attrs={
				"class":"form-control my-2",
				"placeholder":"MailId",
			}),
			"mble":forms.TextInput(attrs={
				"class":"form-control my-2",
				"placeholder":"Mobile Number",
			}),
			"gdr":forms.Select(attrs={
				"class":"form-control my-2",
			}),
		}
class DonorForm(forms.ModelForm):
	class Meta:
		model=Donorpfl
		fields=["bloodgroup","address"]
		widgets={
			"bloodgroup":forms.TextInput(attrs={
				"class":"form-control my-2",
				"placeholder":"blood group",
			}),
			"address":forms.TextInput(attrs={
				"class":"form-control my-2",
				"placeholder":"Address",
			}),
		}
class StaffForm(forms.ModelForm):
	class Meta:
		model=Staffpfl
		fields=["s_num","quali"]
		widgets={
			"s_num":forms.TextInput(attrs={
				"class":"form-control my-2",
				"placeholder":"Staff Id",
			}),
			"quali":forms.TextInput(attrs={
				"class":"form-control my-2",
				"placeholder":"Qualifications",
			}),
		}
class MedicalForm(forms.ModelForm):
	class Meta:
		model=Med_per
		fields=["M_num","quali","Med_Li_Num"]
		widgets={
			"M_num":forms.TextInput(attrs={
				"class":"form-control my-2",
				"placeholder":"Medical Id",
			}),
			"quali":forms.TextInput(attrs={
				"class":"form-control my-2",
				"placeholder":"Quali with spec",
			}),
			"Med_Li_Num":forms.TextInput(attrs={
				"class":"form-control my-2",
				"placeholder":"Licence Number",
			}),
		}
class Requests(forms.ModelForm):
	class Meta:
		model=Bloodrequests
		fields=["patient_name","patient_age","bloodgroup","unit","disease"]
		widgets={
			"patient_name":forms.TextInput(attrs={
				"class":"form-control my-2",
				"placeholder":"Patient Name",
			}),
			"patient_age":forms.NumberInput(attrs={
				"class":"form-control my-2",
				"placeholder":"Patient Age",
			}),
			"bloodgroup":forms.TextInput(attrs={
				"class":"form-control my-2",
				"placeholder":"Blood Group",
			}),
			"unit":forms.NumberInput(attrs={
				"class":"form-control my-2",
				"placeholder":"Units",
			}),
			"disease":forms.TextInput(attrs={
				"class":"form-control my-2",
				"placeholder":"Disease",
			}),
		}

class UpreqForm(forms.ModelForm):
	class Meta:
		model = Bloodrequests
		fields = ["bloodgroup","status","Med_perdesc"]
		widgets = {
		"bloodgroup":forms.TextInput(attrs={
			"class":"form-control my-2",
			"readonly":"true",
			}),
		"status":forms.Select(attrs={
			"class":"form-control my-2",
			}),
		"Med_perdesc":forms.Textarea(attrs={
			"class":"form-control my-2",
			"rows":"3",
			}),
		}

class Donors(forms.ModelForm):
	class Meta:
		model=Donate
		fields=["donor_name","donor_age","blood_group","units","diseases"]
		widgets={
			"donor_name":forms.TextInput(attrs={
				"class":"form-control my-2",
				"placeholder":"Donor Name",
			}),
			"donor_age":forms.NumberInput(attrs={
				"class":"form-control my-2",
				"placeholder":"Donor Age",
			}),
			"blood_group":forms.TextInput(attrs={
				"class":"form-control my-2",
				"placeholder":"Blood Group",
			}),
			"units":forms.NumberInput(attrs={
				"class":"form-control my-2",
				"placeholder":"Units",
			}),
			"diseases":forms.TextInput(attrs={
				"class":"form-control my-2",
				"placeholder":"Diseases",
			}),
		}
class UpDonorForm(forms.ModelForm):
	class Meta:
		model = Donate
		fields = ["blood_group","status","Med_perdesc"]
		widgets = {
		"blood_group":forms.TextInput(attrs={
			"class":"form-control my-2",
			"readonly":"true",
			}),
		"status":forms.Select(attrs={
			"class":"form-control my-2",
			}),
		"Med_perdesc":forms.Textarea(attrs={
			"class":"form-control my-2",
			"rows":"3",
			}),
		}
class ChgPwdForm(PasswordChangeForm):
	old_password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Old Password"}))
	new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"New Password"}))
	new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Password Again"}))
	class Meta:
		model = User
		fields = "__all__"
class BloodStockForm(forms.ModelForm):
	class Meta:
		model = BloodStock
		fields = ["blood_group","units"]
		widgets = {
			"blood_group":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Blood Group"
			}),
			"units":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Units"
			}),
		}