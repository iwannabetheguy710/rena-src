from django.contrib import admin
from django.contrib.auth.models import *
from django import forms

from .models import *
from home.admin import *
from martor.widgets import AdminMartorWidget

class TestCaseForm(forms.ModelForm):
	class Meta:
		widgets = {
			'problem': forms.TextInput(attrs={'size': 100})
		}


class TestCaseAdmin(admin.ModelAdmin):
	formfield_overrides = {
		models.TextField: {'widget': AdminMartorWidget},
	}
	form = TestCaseForm

# Register your models here.
admin.site.register(Testcase, TestCaseAdmin)
admin.site.register(Submission)