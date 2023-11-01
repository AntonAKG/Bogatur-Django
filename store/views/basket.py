from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


from store.models import BasketTicket, BasketCoach
@method_decorator(login_required, name='dispatch')
class BasketView(TemplateView):
    template_name = 'basket/basket.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Корзина'
        context['coach_basket'] = BasketCoach.objects.filter(user_id=self.request.user.id)
        context['ticket_basket'] = BasketTicket.objects.filter(user_id=self.request.user.id)

        return context
