from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import Index, About, Contact, CoachView, CoachDetail, TicketView, LoginClassView, Register, ProfileView

urlpatterns = [
    path('', Index.as_view(), name='main'),
    path('about/', About.as_view(), name='about'),
    path('contact/', Contact.as_view(), name='contact'),
    path('coach/', CoachView.as_view(), name='coach'),
    path('coach/<slug:coach_slug>/', CoachDetail.as_view(), name='coach_detail'),
    path('ticket/', TicketView.as_view(), name='ticket'),
    path('register/', Register.as_view(), name="register"),
    path('login/', LoginClassView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
