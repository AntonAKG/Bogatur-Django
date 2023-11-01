from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from store.forms import RegisterForm, LoginForm
from django.contrib.auth.views import LoginView
from django.urls import reverse


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
