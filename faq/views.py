from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact, FAQ

def faq_view(request):
    faqs = FAQ.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact = Contact(name=name, email=email, message=message)
        contact.save()

        messages.success(request, 'Your message has been sent. Thank you!')

        return redirect('faq')

    return render(request, 'faq/faq.html', {'faqs': faqs})