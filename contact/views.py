from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save the contact in the database
        contact = Contact(name=name, email=email, message=message)
        contact.save()

        # Send an email
        send_mail(
            subject=f'Message from {name}',
            message=message,
            from_email=email,
            recipient_list=['andersmiller@gmail.com'],
        )

        messages.success(request, 'Your message has been sent. Thank you!')
        return redirect('contact')

    return render(request, 'contact/contact.html')