from django.http import HttpResponseRedirect, HttpResponse
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from datetime import datetime, timedelta

from store.models import Ticket, ActiveTicket

@method_decorator(login_required, name='dispatch')
class AddActiveTicket(View):

    @staticmethod
    def get(request, ticket_id):
        ticket_exists = Ticket.objects.filter(id=ticket_id).exists()

        if ticket_exists:
            today = datetime.now()
            end_start = today + timedelta(days=30)

            formatted_date = today.strftime('%Y%m%d')
            format_end = end_start.strftime('%Y%m%d')

            ActiveTicket.create(ticket_id=ticket_id, user=request.user, start_date=formatted_date,
                                end_date=format_end)

            return HttpResponseRedirect(request.META['HTTP_REFERER'])

        else:

            return HttpResponse('asfwgv')