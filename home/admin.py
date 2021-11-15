from django.contrib import admin
from django.contrib.auth.models import *
from django import forms

from .models import *
from martor.widgets import AdminMartorWidget

class BlogAdmin(admin.ModelAdmin):
	formfield_overrides = {
		models.TextField: {'widget': AdminMartorWidget},
	}

class ProfileAdmin(admin.ModelAdmin):
	search_fields = ['user__username']
	autocomplete_fields = ["user"]

class ProblemAdmin(admin.ModelAdmin):
	search_fields = ['user_id', 'user__username']
	autocomplete_fields = ["author"]
	formfield_overrides = {
		models.TextField: {'widget': AdminMartorWidget},
	}

# Register your models here.
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Problem, ProblemAdmin)
admin.site.register(Blog, BlogAdmin)