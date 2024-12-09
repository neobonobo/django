from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Exchange, Settlement, get_user_model

User = get_user_model()

@login_required
def exchange_history(request, user1_id, user2_id):
    user1 = get_object_or_404(User, id=user1_id)
    user2 = get_object_or_404(User, id=user2_id)

    # Fetch unsettled exchanges between user1 and user2
    exchanges = Exchange.objects.filter(
        giver__in=[user1, user2],
        receiver__in=[user1, user2],
        is_settled=False
    ).order_by('timestamp')

    # Calculate balance
    settlement = Settlement(user1=user1, user2=user2)
    settlement.calculate_balance()

    return render(request, 'exchanges/history.html', {
        'user1': user1,
        'user2': user2,
        'exchanges': exchanges,
        'settlement': settlement,
    })

@login_required
def settle_exchanges(request, user1_id, user2_id):
    user1 = get_object_or_404(User, id=user1_id)
    user2 = get_object_or_404(User, id=user2_id)

    # Fetch or create a settlement and settle exchanges
    settlement, _ = Settlement.objects.get_or_create(user1=user1, user2=user2)
    settlement.settle_exchanges()

    return redirect('exchange_history', user1_id=user1.id, user2_id=user2.id)
