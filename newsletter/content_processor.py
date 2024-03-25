from .forms import NewsletterForm


def newsletter_context(request):
    newsletter_form = NewsletterForm()
    return {"newsletter_form": newsletter_form}
