from django import forms

class TestCaseForm(forms.ModelForm):
	class Meta:
		widgets = {'problem': forms.TextChoice(attrs={'size': 100})
					}
