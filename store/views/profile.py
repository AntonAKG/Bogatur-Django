from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from datetime import datetime

from store.forms import UserProfileForm
from store.models import ActiveTicket, User, ActiveCoach


@method_decorator(login_required, name='dispatch')
class ProfileView(TemplateView):
    template_name = 'profile/profile.html'

    def get_context_data(self, **kwargs):
        today = datetime.now()

        # formatted_date = today.strftime('%Y%m%d')
        # format_end = end_start.strftime('%Y%m%d')
        current_date = today.strftime('%Y%m%d')

        context = super().get_context_data(**kwargs)
        context['title'] = 'Profile'
        context['form'] = UserProfileForm(instance=self.request.user)
        context['active_ticket'] = ActiveTicket.objects.filter(user_id=self.request.user.id)
        context['active_coach'] = ActiveCoach.objects.filter(user_id=self.request.user.id)
        context['current_date'] = current_date
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
