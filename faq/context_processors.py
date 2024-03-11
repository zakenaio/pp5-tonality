from .models import Newsletter

def newsletter_context(request):
    # Query your Newsletter model here
    newsletters = Newsletter.objects.all()
    # Return a context dictionary that will be added to the template context
    return {'newsletters': newsletters}