from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import Index

urlpatterns = [
    path('', Index.as_view(), name='main'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
