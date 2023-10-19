from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate
from django.urls import reverse

from .models import Coach, Ticket
from .forms import RegisterForm, LoginForm


class Index(View):
    templates_name = 'main_menu/main.html'

    def get(self, request):
        context = {
            'title': "Головна сторінка"
        }

        return render(request=request, context=context, template_name=self.templates_name)


class About(View):
    templates_name = r'main_menu/about.html'

    def get(self, request):
        context = {
            'title': 'About'
        }

        return render(request=request, context=context, template_name=self.templates_name)


class Contact(View):
    templates_name = r'main_menu/contact.html'

    def get(self, request):
        context = {
            'title': 'Контакти'
        }
        return render(request=request, context=context, template_name=self.templates_name)


class CoachView(ListView):
    model = Coach
    template_name = 'coach/coach.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CoachView, self).get_context_data(**kwargs)

        context['title'] = "Тренера"

        return context


class CoachDetail(DetailView):
    model = Coach
    template_name = 'coach/coach_detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'coach_slug'
    context_object_name = 'coach'


class TicketView(ListView):
    model = Ticket
    template_name = 'ticket/ticket.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TicketView, self).get_context_data(**kwargs)

        context['title'] = "Ticket"

        return context


class Register(View):
    template_name = r'registration\register.html'

    def get(self, request):
        context = {
            'title': 'Register',
            'form': RegisterForm()
        }

        return render(request, self.template_name, context=context)

    def post(self, request):
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()

            password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            authenticate(password=password, email=email)
            # login(request, user)
            return redirect('login')

        context = {
            'title': 'Register',
            'form': form
        }

        return render(request, self.template_name, context=context)


class LoginClassView(LoginView):
    LoginView.authentication_form = LoginForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Login'

        return context

    def get_success_url(self):
        return reverse('profile')


class ProfileView(TemplateView):
    template_name = 'profile/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Profile'
        return context
