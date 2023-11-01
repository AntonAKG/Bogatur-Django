from django.views.generic import ListView

from store.models import Ticket

class TicketView(ListView):
    model = Ticket
    template_name = 'ticket/ticket.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TicketView, self).get_context_data(**kwargs)

        context['title'] = "Ticket"

        return context
