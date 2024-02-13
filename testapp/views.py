from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView,ListView,CreateView,DetailView,UpdateView,DeleteView
from testapp .models import Student
from django.urls import reverse_lazy

# Create your views here.
from django.http import HttpResponse

class Hello_View(View):
    def get(self,request):
        return HttpResponse("<h1>Hello Response from class based view</h1>")


class Temp_View(TemplateView):
    template_name = "testapp/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"]="Aditya"
        context["rollno"]=111
        context["subject"]="Python"
        return context

class StudentList_View(ListView):
    model=Student


class Student_Create(CreateView):
    model = Student
    fields='__all__'

class Student_Details(DetailView):
    model=Student
    #context_object_name = 'student'

class Student_Update(UpdateView):
    model=Student
    fields=('sname','smarks')

class Student_Delete(DeleteView):
    model =Student
    success_url=reverse_lazy('list')

