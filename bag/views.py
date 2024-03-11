from django.shortcuts import render, redirect
from records.models import Records  # Adjusted import for Record model from another app

def view_bag(request):
    """ A view that renders the bag contents page """
    bag = request.session.get('bag', {})
    bag_items = []
    total = 0
    product_count = 0

    for item_id, quantity in bag.items():
        try:
            record = Records.objects.get(id=item_id)  # Fetching the Record based on item_id
            total += quantity * record.price
            product_count += quantity
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
        'product_count': product_count,
    }

    return render(request, 'bag/bag.html', context)


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)