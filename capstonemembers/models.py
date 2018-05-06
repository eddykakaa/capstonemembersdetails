from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf.urls import *


class MembersDetails(models.Model):
	STATUS_CHOICES = (
		('draft','Draft'),
		('confirmed','Confirmed'),
	)
	SEX_CHOICES = (
		('male','Male'),
		('female','Female'),
	)
	MARRIAGE_CHOICES = (
		('married','Married'),
		('single','Single'),
	)
	OCCUPATION_CHOICES = (
		('employed','Employed'),
		('business','Business'),
		('epxertise','Expertise'),
		('student','Student'),
		('others','Others'),

	)
	LANGUAGE_CHOICES = (
		('english','English'),
		('swahili','Swahili'),
		('french','French'),
		('others','Others'),

	)
	YESNO_CHOICES = (
		('yes','Yes'),
		('no','No'),

	)

	firstname = models.CharField(max_length=250)
	secondname = models.CharField(max_length=250)
	lastname = models.CharField(max_length=250)
	physical_address = models.CharField(max_length=250)
	postaladdress = models.CharField(max_length=250,blank=True,null = True)
	phonenumber1 = models.CharField(max_length=10,blank=True,null = True)
	phonenumber2 = models.CharField(max_length=10,blank=True,null = True)
	phonenumber3 = models.CharField(max_length=10,blank=True,null = True)
	emailaddress = models.CharField(max_length=250)
	birthdate = models.DateField()
	nationality = models.CharField(max_length=250)
	spousename = models.CharField(max_length=250)
	author = models.ForeignKey(User,related_name='blog_posts',on_delete=models.CASCADE)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
	gender = models.CharField(max_length=10,choices=SEX_CHOICES)
	marriage = models.CharField(max_length=10,choices=MARRIAGE_CHOICES)
	occupation = models.CharField(max_length=10,choices=OCCUPATION_CHOICES)
	occupationdetails = models.CharField(max_length=250)
	languages = models.CharField(max_length=10,choices=LANGUAGE_CHOICES)
	datejoiningcapstone = models.DateField()
	fellowshipname = models.CharField(max_length=250)
	bornagain = models.CharField(max_length=10,choices=YESNO_CHOICES)
	filledhollyspirit = models.CharField(max_length=10,choices=YESNO_CHOICES)
	baptisedimmersion = models.CharField(max_length=10,choices=YESNO_CHOICES)
	servinggoddept = models.CharField(max_length=250)
	havingchildren = models.CharField(max_length=10,choices=YESNO_CHOICES)




	class Meta:
		ordering = ('-publish',)

	def __str__(self):
		return self.firstname
