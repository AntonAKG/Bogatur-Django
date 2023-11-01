from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from django.http import HttpResponseRedirect

from store.models import BasketCoach
@method_decorator(login_required, name='dispatch')
class BasketCoachAddView(View):

    @staticmethod
    def get(request, coach_id, coach_slug):
        BasketCoach.create_or_update(coach_id, request.user)
        return redirect('basket')


@method_decorator(login_required, name='dispatch')
class BasketCoachDelView(View):

    @staticmethod
    def get(request, coach_id):
        basket = BasketCoach.objects.get(id=coach_id)
        basket.delete()
        return HttpResponseRedirect(request.META['HTTP_REFERER'])