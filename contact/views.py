from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
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
            message=f"From: {email}\n\nMessage:\n{message}",
            from_email='andersmiller@gmail.com',
            recipient_list=['andersmiller@gmail.com'],
            fail_silently=False,
        )

        messages.success(request, 'Your message has been sent. Thank you!')
        
        # Redirect back to the same page
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

    return render(request, 'contact/contact.html')