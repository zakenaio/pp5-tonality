from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin
from .models import Newsletter

class NewsletterMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.method == 'POST' and 'q' in request.POST:
            email = request.POST.get('q')
            Newsletter.objects.get_or_create(email=email)
            return redirect(request.path_info)