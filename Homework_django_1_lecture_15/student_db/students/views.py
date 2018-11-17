from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Student
from django.urls import reverse
from .forms import NewStudentForm
# Create your views here.


class IndexView(ListView):
    model = Student
    template_name = 'index.html'

class StudentDetailView(DetailView):
    model = Student
    template_name = 'detail.html'

class StudentCreateView(CreateView):
    model = Student
    template_name = 'add_student.html'
    form_class = NewStudentForm

    def get_success_url(self):
        return reverse('index')