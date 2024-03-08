from django.shortcuts import render
from .models import Records


def all_records(request):
    """View for all records"""

    records = Records.objects.all()

    context = {
        'records': records,
    }

    return render(request, 'records/records.html', context)