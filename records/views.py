from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Records


def all_records(request):
    """View for all records"""

    records = Records.objects.all()
    query = ''
    category = request.GET.get('category', '')

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q'].strip()
            if not query and not category:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('records'))
            
            if query:
                if query == 'is_new_release,deals':
                    records = records.filter(Q(is_new_release=True) | Q(is_deal=True))
                elif query == 'is_new_release':
                    records = records.filter(is_new_release=True)
                elif query == 'deals':
                    records = records.filter(is_deal=True)
                else:
                    queries = (
                        Q(name__icontains=query) |
                        Q(description__icontains=query) |
                        Q(category__name__icontains=query)
                    )
                    records = records.filter(queries).distinct()
        elif category:
            records = records.filter(category__name__icontains=category).distinct()

    context = {
        'records': records,
        'search_term': query or category,
    }

    return render(request, 'records/records.html', context)

def record_detail(request, record_id):
    """ A view to show individual record details """

    record = get_object_or_404(Records, pk=record_id)

    context = {
        'record': record,
    }

    return render(request, 'records/record_detail.html', context)

