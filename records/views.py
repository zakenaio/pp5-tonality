from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Records, Category
from .forms import RecordForm


def all_records(request):
    """View for all records"""

    records = Records.objects.all()
    query = None
    sort = None
    direction = None

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
            records = records.order_by(sortkey).distinct()

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            records = records.filter(category__name__in=categories).distinct()

        if 'q' in request.GET:
            query = request.GET['q'].strip().lower()
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!"
                    )
                return redirect(reverse('records'))

            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(category__name__icontains=query)
            records = records.filter(queries).distinct()

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


@login_required
def add_record(request):
    """ Add a record to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = RecordForm(request.POST, request.FILES)
        if form.is_valid():
            record = form.save()
            messages.success(request, 'Successfully added record!')
            return redirect(reverse('record_detail', args=[record.id]))
        else:
            messages.error(
                request,
                'Failed to add record. Please ensure the form is valid.'
                )
    else:
        form = RecordForm()

    template = 'records/add_record.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_record(request, record_id):
    """ Edit a record in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    record = get_object_or_404(Records, pk=record_id)
    if request.method == 'POST':
        form = RecordForm(request.POST, request.FILES, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated record!')
            return redirect(reverse('record_detail', args=[record.id]))
        else:
            messages.error(
                request,
                'Failed to update record. Please ensure the form is valid.'
                )
    else:
        form = RecordForm(instance=record)
        messages.info(request, f'You are editing {record.name}')

    template = 'records/edit_record.html'
    context = {
        'form': form,
        'record': record,
    }

    return render(request, template, context)


@login_required
def delete_record(request, record_id):
    """ Delete a record from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    record = get_object_or_404(Records, pk=record_id)
    record.delete()
    messages.success(request, 'Record deleted!')
    return redirect(reverse('records'))
