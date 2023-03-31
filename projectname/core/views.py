from django.shortcuts import render
from django.views.generic import DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .models import Member, Appointment
from .forms import AppointmentForm


class MemberDetailView(LoginRequiredMixin, DetailView):
    model = Member
    template_name = 'member_detail.html'
    context_object_name = 'member'
    login_url = reverse_lazy('login')


class AppointmentCreateView(LoginRequiredMixin, CreateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'appointment_create.html'
    success_url = reverse_lazy('book')
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        form.instance.member = self.request.user.member
        return super().form_valid(form)
    
class LoginView(LoginView):
    template_name = 'login.html' # specify the template for rendering the login form
    success_url = reverse_lazy('home') # specify the URL to redirect to after successful login
    redirect_authenticated_user = True # redirect authenticated users to the success URL

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Login' # specify a page title for the login form
        return context