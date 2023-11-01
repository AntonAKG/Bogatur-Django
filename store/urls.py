from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

from store.views import active_ticket, home, auth, basket, basket_coach, basket_ticket, coach, ticket, profile

urlpatterns = [
      # Home
    path('', home.Home.as_view(), name='main'),
    path('about/', home.About.as_view(), name='about'),
    path('contact/', home.Contact.as_view(), name='contact'),

    # coach

    path('coach/', coach.CoachView.as_view(), name='coach'),
    path('coach/<slug:coach_slug>/', coach.CoachDetail.as_view(), name='coach_detail'),

    # ticket

    path('ticket/', ticket.TicketView.as_view(), name='ticket'),

    # Auth

    path('', include('django.contrib.auth.urls')),
    path('register/', auth.Register.as_view(), name="register"),
    path('login/', auth.LoginClassView.as_view(), name='login'),

    # profile

    path('profile/', login_required(profile.ProfileView.as_view()), name='profile'),


    # basket

    path('basket/', basket.BasketView.as_view(), name='basket'),

    # basket coach(add, remove)

    path('coach/<slug:coach_slug>/add/<int:coach_id>', basket_coach.BasketCoachAddView.as_view(),name='coach_add'),
    path('basket/delete_coach/<int:coach_id>', basket_coach.BasketCoachDelView.as_view(),name='coach_delete'),

    # basket ticket(add, remove)

    path('basket/add/<int:ticket_id>', basket_ticket.BasketAddView.as_view(), name='basket_add'),
    path('basket/remove/<int:basket_id>', basket_ticket.BasketRemoveView.as_view(), name='basket_remove'),

    # add active ticket

    path('basket/buy_ticket/add_active/<int:ticket_id>', active_ticket.AddActiveTicket.as_view(), name='add_active')

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
