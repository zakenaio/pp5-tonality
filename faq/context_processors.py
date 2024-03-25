from .models import FAQ


def faq_processor(request):
    faqs = FAQ.objects.all()
    return {'faqs': faqs}
