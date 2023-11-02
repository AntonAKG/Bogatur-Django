from django.http import HttpResponse
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect, render

from store.models import Coach, ActiveCoach
from store.forms import AddTrainingSessionForm


@method_decorator(login_required, name='dispatch')
class ActiveCoachView(View):
    def get(self, request, coach_id):
        coach_exists = Coach.objects.filter(id=coach_id)
        print(coach_exists)

        if not coach_exists:
            return redirect('profile')  # Return a response to redirect the user

        return HttpResponse("Coach not found or other error message")

    def post(self, request, coach_id):
        coach_exists = Coach.objects.filter(id=coach_id)
        if not coach_exists:
            return redirect('profile')  # Return a response to redirect the user

        form = AddTrainingSessionForm(request.POST)
        if form.is_valid():
            user = request.user
            coach = Coach.objects.get(id=coach_id)

            amount_of_training = form.cleaned_data['amount_of_training']

            ActiveCoach.objects.get_or_create(user=user, coach=coach,
                                                          amount_of_training=amount_of_training, price=coach.price_per_training*amount_of_training)

            return redirect('profile')
