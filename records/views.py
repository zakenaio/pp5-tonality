from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Records, Category
from django.db.models.functions import Lower

def all_records(request):
    """View for all records"""

    records = Records.objects.all()
    query = None
    sort = None
    direction = None

    # Fetch all categories to display on the page, regardless of filtering
    all_categories = Category.objects.all()

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                records = records.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if sortkey == 'release':
                sortkey = 'releasedate'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            records = records.order_by(sortkey)
            
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            records = records.filter(category__name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q'].strip().lower()  # Normalize the query for case-insensitive search
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('records'))
            
            # Generalized search logic that looks for the query in various fields
            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(category__name__icontains=query)
            records = records.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'records': records,
        'search_term': query,
        'all_categories': all_categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'records/records.html', context)

def record_detail(request, record_id):
    """ A view to show individual record details """

    record = get_object_or_404(Records, pk=record_id)

    context = {
        'record': record,
    }

    return render(request, 'records/record_detail.html', context)

