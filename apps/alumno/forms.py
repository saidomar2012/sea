from django import forms
from apps.alumno.models import alumno

class AlumnoForm(forms.ModelForm):

	class Meta:
			model = alumno

			fields = [
				'Identidad',
				'nombres',
				'apellidos',
				'fechaNac',
				'sexo',
			]
			labels = {
				'Identidad': 'identidad',
				'nombres': 'nombres', 
				'apellidos': 'apellidos',
				'fechaNac': 'Fecha de Nacimiento',
				'sexo':'sexo',
			}
			widgets = {
				'Identidad':forms.TextInput(attrs={'class':'form-control'}),
				'nombres':forms.TextInput(attrs={'class':'form-control'}),
				'apellidos':forms.TextInput(attrs={'class':'form-control'}),
				'fechaNac':forms.TextInput(attrs={'class':'form-control'}),
				'sexo': forms.Select(attrs={'class':'form-control'}),
			}


			
