from django.urls import path
from .views import faq_view
from . import views

urlpatterns = [
    path('', faq_view, name='faq'),
]
