from django import template
from main.models import Pedido

register = template.Library()


@register.filter
def cart_item_count(user):
    if user.is_authenticated:
        qs = Pedido.objects.filter(user=user, ordered=False)
        if qs.exists():
            return qs[0].items.count()
    return 0
