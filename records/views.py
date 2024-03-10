from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Records


def all_records(request):
    """View for all records"""

    records = Records.objects.all()
    query = ''

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q'].strip()
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('records'))
            
            queries = (
                Q(name__icontains=query) |
                Q(description__icontains=query) |
                Q(category__name__icontains=query)
            )
            records = records.filter(queries).distinct()

    context = {
        'records': records,
        'search_term': query,
    }

    return render(request, 'records/records.html', context)

def record_detail(request, record_id):
    """ A view to show individual record details """

    record = get_object_or_404(Records, pk=record_id)

    context = {
        'record': record,
    }

    return render(request, 'records/record_detail.html', context)
