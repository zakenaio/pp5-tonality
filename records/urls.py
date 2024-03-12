from django.urls import path
from . import views

urlpatterns = [
    path('', views.Records, name='records'),
    path('<int:record_id>/', views.record_detail, name='record_detail'),
    path('add/', views.add_record, name='add_record'),
    path('edit/<int:record_id>/', views.edit_record, name='edit_record'),
    path('delete/<int:record_id>/', views.delete_record, name='delete_record'),
]