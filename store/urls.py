from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

from .views import (Index, About, Contact, CoachView, CoachDetail, TicketView, LoginClassView, Register, ProfileView,
                    TicketDetail, BasketAddView, BasketRemoveView, BasketView, BuyTicketView, BasketCoachAddView, BasketCoachDelView)

urlpatterns = [
    path('', Index.as_view(), name='main'),
    path('about/', About.as_view(), name='about'),
    path('contact/', Contact.as_view(), name='contact'),

    path('coach/', CoachView.as_view(), name='coach'),
    path('coach/<slug:coach_slug>/', CoachDetail.as_view(), name='coach_detail'),
    path('coach/<slug:coach_slug>/add/<int:coach_id>', BasketCoachAddView.as_view(), name='coach_add'),
    path('basket/delete_coach/<int:coach_id>', BasketCoachDelView.as_view(), name='coach_delete'),

    path('ticket/', TicketView.as_view(), name='ticket'),
    path('ticket/<slug:ticket_slug>', TicketDetail.as_view(), name='ticket_detail'),

    path('register/', Register.as_view(), name="register"),
    path('login/', LoginClassView.as_view(), name='login'),
    path('profile/', login_required(ProfileView.as_view()), name='profile'),
    path('', include('django.contrib.auth.urls')),

    path('basket/', BasketView.as_view(), name='basket'),
    path('basket/add/<int:ticket_id>', BasketAddView.as_view(), name='basket_add'),
    path('basket/remove/<int:basket_id>', BasketRemoveView.as_view(), name='basket_remove'),
    path('basket/buy_ticket/', BuyTicketView.as_view(), name='buy_ticket')


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
