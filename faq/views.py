from django.shortcuts import render, redirect
from django.contrib import messages
from .models import FAQ

def faq_view(request):
    faqs = FAQ.objects.all()


    return render(request, 'faq/faq.html', {'faqs': faqs})