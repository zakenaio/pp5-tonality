from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from django.core.mail import send_mail
from .forms import NewsletterForm

def newsletter_subscribe(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            subscription = form.save()
            
            send_mail(
                'Welcome to Our Newsletter',
                'Thank you for subscribing to our newsletter! You will now receive the latest updates directly to your inbox.',
                'subscribe@tonality.example.com',
                [subscription.email],
                fail_silently=False,
            )
            messages.success(request, 'Thank you for subscribing, a welcome mail has been sent!')
            return redirect(reverse('home'))
    else:
        form = NewsletterForm()

    return redirect(reverse('home')) 