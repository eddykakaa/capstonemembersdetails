from django.contrib import admin

from .models import MembersDetails

class MembersDetailsAdmin(admin.ModelAdmin):
	list_display = ('firstname','secondname','lastname','postaladdress','phonenumber1','emailaddress','birthdate','gender','datejoiningcapstone','bornagain')



admin.site.register(MembersDetails, MembersDetailsAdmin)
