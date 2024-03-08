from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_records, name='records'),
    path('<record_id>', views.record_detail, name='record_detail'),
]

