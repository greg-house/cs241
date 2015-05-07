from django.db import models
from django.core.validators import RegexValidator

class SuperUser(models.Model):
	name = models.CharField(max_length=10,unique=True)
	password = models.CharField(max_length=30, null=True)
	def __str__(self):
		return self.name

class Department(models.Model):
	name = models.CharField(max_length = 30)
	id = models.CharField(unique=True, max_length=3, primary_key=True)
	def __str__(self):
		return self.id

class Designation(models.Model):
	name = models.CharField(max_length = 30)
	def __str__(self):
		return self.name

class Student(models.Model):
	name = models.CharField(max_length=40, validators=[RegexValidator(regex=r'^[a-zA-Z\s]+$', message="No special characters or Numbers")])
	Male = 'Male'
	Female = 'Female'
	choice = ( 
			(Male,'Male'),
			(Female,'Female'),
		)
	sex = models.CharField(max_length=6,choices=choice,default=Male)
	roll_no = models.CharField(unique=True, max_length=8, primary_key=True, validators=[RegexValidator(regex=r'^\d{4}[a-zA-Z]{2}\d{2}$', message="1301xxXX")])
	year_of_registration = models.DateField('Date Joined(MM/DD/YYYY)')
#	contact_no = models.PositiveIntegerField(default=0)
#	phone_regex = RegexValidator(regex=r'^\d{10}$', message="10 digit mobile number or 11 digit landline number")
	contact_no = models.CharField(max_length=10, validators=[RegexValidator(regex=r'^\d{10}$', message="10 digit mobile number")], blank=True) #	validators should be a list
	emailID = models.CharField(max_length=30, validators=[RegexValidator(regex=r'^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9.]+$', message="Enter valid email id")])
	dept = models.ForeignKey(Department)
#	stipend = models.PositiveIntegerField(default=0)
	password = models.CharField(max_length=30, null=True)
#	project = models.ManyToManyField('Project', null=True)
	def __str__(self):
		return self.name

class Professor(models.Model):		
	name = models.CharField(max_length=40, validators=[RegexValidator(regex=r'^[a-zA-Z\s]+$', message="No special characters or Numbers")])
	Male = 'Male'
	Female = 'Female'
	choice = ( 
			(Male,'Male'),
			(Female,'Female'),
		)
	sex = models.CharField(max_length=6,choices=choice,default=Male)
	designation = models.ForeignKey('Designation')
	department = models.ManyToManyField(Department)
	emp_no = models.CharField(unique=True, max_length=8, primary_key=True, validators=[RegexValidator(regex=r'^[a-zA-Z]{2}\d{3}$', message="eeXXX")])
	year_of_joining = models.DateField('Date Joined(MM/DD/YYYY)')
#	contact_no = models.PositiveIntegerField(default=0)
	phone_regex = RegexValidator(regex=r'^\d{10}$', message="10 digit mobile number")
	contact_no = models.CharField(max_length=10, validators=[phone_regex], blank=True) # validators should be a list
	emailID = models.CharField(max_length=30, validators=[RegexValidator(regex=r'^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9.]+$', message="Enter valid email id")])
	acc_no = models.CharField(max_length=16, validators=[RegexValidator(regex=r'^\d{10,16}$', message="10-16 digit account number")])
	password = models.CharField(max_length=30, null=True)
#	project = models.ManyToManyField('Project', null=True)
	def __str__(self):
		return self.name

class Vendor(models.Model):
	name = models.CharField(max_length=40, validators=[RegexValidator(regex=r'^[a-zA-Z\s]+$', message="No special characters or Numbers")])
	id = models.AutoField(unique=True,max_length=4,primary_key=True)
	password = models.CharField(max_length=30, null=True)
	Address = models.TextField()
#	validators=[RegexValidators(regex=r'^[a-zA-Z\s0-9\-]+$', message="No special characters")]
#	PhoneNo = models.PositiveIntegerField(default=0)
	phone_regex = RegexValidator(regex=r'^\d{10,11}$', message="10 digit mobile number or 11 digit landline number")
	PhoneNo = models.CharField(max_length=11, validators=[phone_regex], blank=True) # validators should be a list
	emailID = models.CharField(max_length=30, validators=[RegexValidator(regex=r'^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9.]+$', message="Enter valid e-mail ID")])
	ShopActRegNo = models.CharField(max_length=15)
	PAN = models.CharField(max_length=10, validators=[RegexValidator(regex=r'^[A-Z]{5}\d{4}[A-Z]{1}$', message="Format: aaaaa9999a")])
	CST = models.CharField(max_length=11, validators=[RegexValidator(regex=r'^\d{11}$', message="11 digit only")])
	VAT = models.CharField(max_length=8)
	BankName = models.CharField(max_length=25)
	BankAddress = models.TextField()
	acc_no = models.CharField(max_length=16, validators=[RegexValidator(regex=r'^\d{10,16}$', message="10-16 digit account number")])
	BranchCode = models.PositiveIntegerField(max_length=6)
	IFSC = models.CharField(max_length=11, validators=[RegexValidator(regex=r'^[A-Z]{4}\d{7}$', message="Format: aaaa999999")])
	def __str__(self):
		return self.name

class Payment(models.Model):                                #payment made by sponsor
	amount = models.PositiveIntegerField(default=0)
	date_payment = models.DateField('Date of Payment(MM/DD/YYYY)')
	sponsorship = models.ForeignKey('Sponsorship')
	def __str__(self):
		return Payment.amount

class Fellowship(models.Model):
	researcher = models.ForeignKey(Student)
	pay = models.PositiveIntegerField(default=0)
	project = models.ForeignKey('Project_Unapproved')
#	sanc_head = models.ForeignKey('Sanctioned_Head')
	def __self__(self):
		return self.researcher

class Project_Unapproved(models.Model):
	id = models.AutoField(unique=True,max_length=3,primary_key=True)
#	file_name = models.CharField(max_length=30)
	project_type = models.CharField(max_length=30)
	title = models.CharField(max_length=50)
	department = models.ManyToManyField(Department)
	description = models.TextField()
	location = models.CharField(max_length=40)
	duration_of_project = models.PositiveIntegerField('Duration in months',default=0)
	updates = models.TextField(null=True)
#	cost_submitted = models.ForeignKey('ExpenseData',null=True)
	PI = models.ForeignKey(Professor)
	co_PI = models.ManyToManyField(Professor,related_name='co_investigator',null=True,blank=True)
	approved = models.PositiveIntegerField(default=0)
	def __str__(self):
		return self.title


class Sponsorship(models.Model):	
	project = models.ForeignKey(Project_Unapproved) 
	sanction_ref_no = models.CharField(max_length=10,unique=True)
	sanction_date = models.DateField('sanction date(MM/DD/YYYY)')
	start_date = models.DateTimeField('date_of_start(MM/DD/YYYY)')
	sponsor = models.ForeignKey('Sponsor')
	amount = models.PositiveIntegerField(default=0)	
	def __str__(self):
		return self.sponsor.name+":"+self.project.title


class Sponsor(models.Model):
	name = models.CharField(max_length=40, validators=[RegexValidator(regex=r'^[a-zA-Z\s]+$', message="No special characters or Numbers")])
	username = models.CharField(max_length=20, primary_key=True, validators=[RegexValidator(regex=r'^[a-zA-Z\s]+$', message="No special characters or Numbers")])
	password = models.CharField(max_length=30, null=True)
	Address = models.TextField()
	phone_regex = RegexValidator(regex=r'^\d{10}$', message="10 digit mobile number")
	PhoneNo = models.CharField(max_length=11, validators=[phone_regex], blank=True) # validators should be a list
	emailID = models.CharField(max_length=30, validators=[RegexValidator(regex=r'^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9.]+$', message="Enter valid email id")])
	PAN = models.CharField(max_length=10, validators=[RegexValidator(regex=r'^[A-Za-z]{5}\d{4}[A-Za-z]{1}$', message="Format: aaaaa9999a")])
	BankName = models.CharField(max_length=25)
	BankAddress = models.TextField()
	acc_no = models.CharField(max_length=16, validators=[RegexValidator(regex=r'^\d{10,16}$', message="10-16 digit account number")])
	BranchCode = models.PositiveIntegerField(max_length=6)
	IFSC = models.CharField(max_length=11, validators=[RegexValidator(regex=r'^[A-Za-z]{4}\d{7}$', message="Format: aaaa999999")])
#	Projects = models.ManyToManyField(Project,through='Sponsorship',through_fields=('sponsor','project'))
	def __str__(self):
		return self.name

class MessageStudProf(models.Model):
	msg_from = models.ForeignKey('Student')
	msg_to = models.ForeignKey('Professor')
	msg = models.TextField()
	project = models.ForeignKey('Project_Unapproved')
	seen = models.BooleanField(default=False)
	def __str__(self):
		return self.pk

class MessageSponsAdmin(models.Model):
	msg_from = models.ForeignKey('Sponsor')
	msg_to = models.CharField(max_length=10)
	msg = models.TextField()
	project = models.ForeignKey('Project_Unapproved')
	seen = models.BooleanField(default=False)
	def __str__(self):
		return self.pk


class Sanctioned_Head(models.Model):
	project = models.ForeignKey(Project_Unapproved)
	name = models.CharField(max_length=20)
	est_amount = models.PositiveIntegerField(default=0)
	appr_amount = models.PositiveIntegerField(default=0)
	given_amt = models.PositiveIntegerField(default=0)
	used_amt = models.PositiveIntegerField(default=0)
	left_amt = models.PositiveIntegerField(default=0)
	def __str__(self):	
		return self.name+" : "+self.project.title


class Purchase(models.Model):
	date = models.DateTimeField('Date(MM/DD/YYYY)')
#	est_cost = models.ForeignKey(Sanctioned_Head,related_name='cost_estimated')
#	sanctioned_cost = models.ForeignKey(Sanctioned_Head,null=True,related_name='cost_sponsored')
	prod_title = models.CharField(max_length=50)
	prod_spec = models.TextField()
	sanc_head = models.ForeignKey(Sanctioned_Head)
	est_cost = models.PositiveIntegerField(default=0)
# add sanction head
	quantity = models.PositiveIntegerField(default=1)
	tot_est_cost = models.PositiveIntegerField(default=0)
#	purchase_no = models.PositiveIntegerField(null=True)
	approval = models.PositiveIntegerField(default=0)	# 0:unapproved 1:approved 2:niq/dp/ten 3:purchaseMade(debitAdviceQueue) -1:rej 	
	def __str__(self):
		return self.prod_title+" : "+self.sanc_head.project.title



# tender & NIQ (both niq and tenders covered letters should be sent to office)

#winner : foreignkey-vendor
# other-participants : many ti many fiekd
#

class Completed_Purchase(models.Model):
#	purchase_no = models.PositiveIntegerField()
	purchase = models.ForeignKey(Purchase)
	vendor = models.ForeignKey(Vendor)
#	others = models.ManyToManyField(Vendor,related_name='other_participants',blank=True)
	cost = models.PositiveIntegerField(default=0,null=True)
	bill_no = models.CharField(max_length=20)
	def __self__(self):
		return self.vendor

class Purchase_duration(models.Model):
	purchase = models.ForeignKey(Purchase)
	NIQ = 'NIQ'
	TENDER = 'tender'
	type_of_purchase_choices = ( 
			(NIQ,'NIQ'),
			(TENDER,'Tender'),
		)
	type_of_purchase = models.CharField(max_length=6,choices=type_of_purchase_choices,default=NIQ)
	release_date = models.DateTimeField('released_date(MM/DD/YYYY)')
	submission_date = models.DateTimeField('last_date(MM/DD/YYYY)')
	result_date = models.DateTimeField('result_date(MM/DD/YYYY)')
	def __self__(self):
		return self.result_date

