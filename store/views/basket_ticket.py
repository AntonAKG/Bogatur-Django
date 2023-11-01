from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

from store.models import BasketTicket
@method_decorator(login_required, name='dispatch')
class BasketAddView(View):
    @staticmethod
    def get(request, ticket_id):
        BasketTicket.create_or_update(ticket_id, request.user)
        return redirect('basket')

@method_decorator(login_required, name='dispatch')
class BasketRemoveView(View):
    def get(self, request, basket_id):
        basket = BasketTicket.objects.get(id=basket_id)
        basket.delete()
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
