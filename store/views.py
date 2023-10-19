from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from .models import Coach, Ticket


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
