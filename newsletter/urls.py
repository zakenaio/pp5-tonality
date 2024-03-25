from django.urls import path
from . import views

urlpatterns = [
    path('newsletter/', views.newsletter_subscribe, name='newsletter'),
]
