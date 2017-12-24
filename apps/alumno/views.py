from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.alumno.forms import AlumnoForm
from apps.alumno.models import alumno


def index(request):
	return render(request, 'alumno/index.html')

def alumno_view(request):
	if request.method == 'POST':
		form = AlumnoForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('alumno:index')
	else:
		form = AlumnoForm()
	return render(request, 'alumno/alumnos_form.html',{'form':form})	

def alumno_list(request):
	alumnos = alumno.objects.all()
	contexto = {'alumnos':alumnos}
	return render(request,'alumno/alumno_list.html',contexto)

def alumno_edit(request, id_alumno):
	alumnos = alumno.objects.get(id=id_alumno)
	if request.method=='GET':
		form = AlumnoForm(instance=alumnos)
	else:
		form= AlumnoForm(request.POST,instance=alumnos)
		if form.is_valid():
			form.save()
		return redirect('alumno:alumno_listar')
	return render(request, 'alumno/alumnos_form.html',{'form':form})

def alumno_delete(request, id_alumno):
	alumnos = alumno.objects.get(id=id_alumno)
	if request.method =='POST':
		alumnos.delete()
		return redirect('alumno:alumno_listar')
	return render(request, 'alumno/alumno_delete.html',{'alumno':alumno})



# listas basada es clases

class AlumnoList(ListView):
	model = alumno
	template_name ='alumno/alumno_list.html'

class AlumnoCreate(CreateView):
	model = alumno
	form_class=AlumnoForm
	template_name ='alumno/alumnos_form.html'
	success_url=reverse_lazy('alumno:alumno_listar')

class AlumnoUpdate(UpdateView):
	model = alumno
	form_class=AlumnoForm
	template_name ='alumno/alumnos_form.html'
	success_url=reverse_lazy('alumno:alumno_listar')

class AlumnoDelete(DeleteView):
	model = alumno
	template_name ='alumno/alumno_delete.html'
	success_url=reverse_lazy('alumno:alumno_listar')

