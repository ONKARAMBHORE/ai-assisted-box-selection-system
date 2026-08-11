from itertools import permutations
from decimal import Decimal
from .models import Box

def dimensions_fit(product, box):
    product_dimensions = [product.length, product.width, product.height,]

    box_dimensions = [ box.length, box.width, box.height, ]

    for dimensions in permutations(product_dimensions):
        if all( product_dimension <= box_dimension for product_dimension, box_dimension in zip(dimensions, box_dimensions)):

            return True

    return False


def recommend_box(order):
    total_weight = Decimal("0")
    total_volume = Decimal("0")

    for item in order.items.select_related("product").all():
        product = item.product

        total_weight += product.weight * item.quantity

        product_volume = (product.length * product.width * product.height)

        total_volume += product_volume * item.quantity

    suitable_boxes = []

    for box in Box.objects.all().order_by("cost"):

        if total_weight > box.max_weight:
            continue

        box_volume = (box.length * box.width * box.height)

        if total_volume > box_volume:
            continue

        all_products_fit = all(
            dimensions_fit(item.product, box)
            for item in order.items.select_related("product").all())

        if all_products_fit:
            suitable_boxes.append(box)

    return suitable_boxes[0] if suitable_boxes else None