from django.shortcuts import render, get_object_or_404
from .models import Records


def all_records(request):
    """View for all records"""

    records = Records.objects.all()

    context = {
        'records': records,
    }

    return render(request, 'records/records.html', context)

def record_detail(request, record_id):
    """ A view to show individual record details """

    record = get_object_or_404(Records, pk=record_id)

    context = {
        'record': record,
    }

    return render(request, 'records/record_detail.html', context)
