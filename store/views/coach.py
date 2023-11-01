from django.views.generic import ListView, DetailView
from store.models import Coach


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
