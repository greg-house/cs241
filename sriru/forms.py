from django import forms
from sriru.models import *
from django.contrib.admin import widgets
from django.views.generic.edit import UpdateView

class ProjectForm(forms.ModelForm):
	class Meta:
		model = Project_Unapproved
		fields = ('project_type','title','description','location','duration_of_project','updates','PI')

class SponsorshipForm(forms.ModelForm):
	class Meta:
		model = Sponsorship

class AddStudent(forms.ModelForm):
	class Meta:
		model = Student
		widgets = {
			'password': forms.PasswordInput(),
		}

class AddProf(forms.ModelForm):
	class Meta:
		model = Professor
		widgets = {
			'password': forms.PasswordInput(),
		}

class SanctionHead(forms.ModelForm):
	class Meta:
		model = Sanctioned_Head
		exclude = ('appr_amount','used_amt','left_amt','given_amt')


class AddVendors(forms.ModelForm):
	class Meta:
		model = Vendor
		widgets = {
			'password': forms.PasswordInput(),
		}

class DeptForm(forms.ModelForm):
	class Meta:
		model = Department

class AddSpons(forms.ModelForm):
	class Meta:
		model = Sponsor
		widgets = {
			'password': forms.PasswordInput(),
		}

class PurchaseForm(forms.ModelForm):
	class Meta:
		model = Purchase
		exclude = ('approval','tot_est_cost')

class PurchaseDurationForm(forms.ModelForm):
	class Meta:
		model = Purchase_duration

class CompletedPurchaseForm(forms.ModelForm):
	class Meta:
		model = Completed_Purchase

class GrantForm(forms.ModelForm):
	class Meta:
		model = Payment

class FellowshipForm(forms.ModelForm):
	class Meta:
		model = Fellowship

class CoPIForm(UpdateView):
	class Meta:
		model = Project_Unapproved
		fields = ['title','co_PI']
		template_name_suffix = '_update_form'

