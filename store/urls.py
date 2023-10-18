from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import Index, About, Contact

urlpatterns = [
    path('', Index.as_view(), name='main'),
    path('about/', About.as_view(), name='about'),
    path('contact/', Contact.as_view(), name='contact')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
