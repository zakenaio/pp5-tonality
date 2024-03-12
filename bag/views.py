from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from records.models import Records

def view_bag(request):
    """ A view that renders the bag contents page """
    bag = request.session.get('bag', {})
    bag_items = []
    total = 0
    record_count = 0

    for item_id, quantity in bag.items():
        try:
            record = Records.objects.get(id=item_id)  # Fetching the Record based on item_id
            total += quantity * record.price
            record_count += quantity
            bag_items.append({
                'item_id': item_id,
                'quantity': quantity,
                'record': record,
            })
        except Records.DoesNotExist:
            # Handle the case where the record does not exist
            pass

    context = {
        'bag_items': bag_items,
        'total': total,
        'record_count': record_count,
    }

    return render(request, 'bag/bag.html', context)


def add_to_bag(request, item_id):
    """ Add a quantity of the specified record to the shopping bag """

    record = Records.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request, f'Updated {record.name} quantity to {bag[item_id]}')
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {record.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified record to the specified amount"""

    record = get_object_or_404(Records, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'record_size' in request.POST:
        size = request.POST['record_size']
    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request, f'Updated {record.name} quantity to {bag[item_id]}')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {record.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        record = get_object_or_404(Records, pk=item_id)
        size = None
        if 'record_size' in request.POST:
            size = request.POST['record_size']
        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(request, f'Removed size {size.upper()} {record.name} from your bag')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {record.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)