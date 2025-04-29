from django.urls import path
from . import views

urlpatterns = [
    path('', views.DoctorListView.as_view(), name='home'),
    path('doctor/add/', views.DoctorCreateView.as_view(), name='add_doctor'),
    path('doctor/<int:pk>/', views.DoctorDetailView.as_view(), name='doctor_detail'),
    path('visit/add/', views.VisitCreateView.as_view(), name='add_visit'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),

]
