from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Coach, Ticket, User, BasketCoach, BasketTicket
from .forms import RegisterForm, LoginForm, UserProfileForm


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


class TicketDetail(DetailView):
    model = Ticket
    template_name = 'ticket/ticket_detail.html'
    slug_field = 'slug'
    slug_url_kwarg = "ticket_slug"
    context_object_name = 'ticket'


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


@method_decorator(login_required, name='dispatch')
class ProfileView(TemplateView):
    template_name = 'profile/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Profile'
        context['form'] = UserProfileForm(instance=self.request.user)
        return context

    @staticmethod
    def post(request: object) -> object:
        form = UserProfileForm(data=request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():

                form.add_error('username', 'Користувач з таким іменем вже існує.')
                form.add_error('email', 'Користувач з такою адресою електронної пошти вже існує.')
            else:

                form.save()
                return redirect('profile')

        return render(request, 'profile/profile.html', {'form': form})


class BasketView(TemplateView):
    template_name = 'basket/basket.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Корзина'
        context['coach_basket'] = BasketCoach.objects.all()
        context['ticket_basket'] = BasketTicket.objects.all()

        return context


@method_decorator(login_required, name='dispatch')
class BasketAddView(View):
    @staticmethod
    def get(request, ticket_id):
        BasketTicket.create_or_update(ticket_id, request.user)
        return HttpResponseRedirect(request.META['HTTP_REFERER'])


# href = "{% url 'products:basket_add' product.id %}" >


@method_decorator(login_required, name='dispatch')
class BasketRemoveView(View):
    def get(self, request, basket_id):
        basket = BasketTicket.objects.get(id=basket_id)
        basket.delete()
        return HttpResponseRedirect(request.META['HTTP_REFERER'])


@method_decorator(login_required, name='dispatch')
class BasketCoachAddView(View):

    @staticmethod
    def get(request, coach_id, coach_slug):
        BasketCoach.create_or_update(coach_id, request.user)
        return HttpResponseRedirect(request.META['HTTP_REFERER'])


@method_decorator(login_required, name='dispatch')
class ConfirmTicket(ListView):
    model = BasketTicket
    template_name = 'basket/confirm_ticket.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['basket'] = BasketTicket.objects.all()

        context['title'] = 'Підтвердження покупки'

        return context
