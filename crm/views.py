from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Doctor, Visit
from django.views.generic import TemplateView
from datetime import date

class DoctorListView(ListView):
    model = Doctor
    template_name = 'crm/doctor_list.html'
    context_object_name = 'doctors'

class DoctorDetailView(DetailView):
    model = Doctor
    template_name = 'crm/doctor_detail.html'

class DoctorCreateView(CreateView):
    model = Doctor
    fields = ['name', 'specialty', 'hospital', 'location', 'email']
    template_name = 'crm/doctor_form.html'
    success_url = reverse_lazy('home')

class VisitCreateView(CreateView):
    model = Visit
    fields = ['doctor', 'date', 'notes', 'next_followup']
    template_name = 'crm/visit_form.html'
    success_url = reverse_lazy('home')

class DashboardView(TemplateView):
    template_name = 'crm/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['doctor_count'] = Doctor.objects.count()
        context['visit_count'] = Visit.objects.count()
        context['upcoming_followups'] = Visit.objects.filter(next_followup__gte=date.today()).order_by('next_followup')[:5]
        return context
