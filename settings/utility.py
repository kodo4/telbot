def _convert(list_convert):

    return [item[0] for item in list_convert]


def get_total_coast(BD):
    """
    Возвращает общую стоимость товара
    """
    # получаем список всех product_id заказа
    all_product_id = BD.select_all_product_id()
    # получаем список стоимость по всем позициям
    # заказа в виде обычного списка
    all_price = [BD.select_single_product_price(item)
                 for item in all_product_id]
    # получаем список количества по всем позициям заказа
    # в виде обычного списка
    all_quantity = [BD.select_order_quantity(item) for item in all_product_id]

    # Возвращает общуб стоимость товара
    return total_coast(all_quantity, all_price)


# считает общую сумму заказа и возвращает результат
def total_coast(list_quantity, list_price):
    order_total_cost = 0
    for ind, item in enumerate(list_price):
        order_total_cost += list_quantity[ind]*list_price[ind]

    return order_total_cost


def get_total_quantity(BD):
    """
    возвращает общее количество заказанной единицы товара
    """
    # получаем список всех product_id
    all_product_id = BD.select_all_product_id()
    # получаем список количества по всем позициям
    # заказа в виде обычного списка
    all_quantity = [BD.select_order_quantity(item) for item in all_product_id]
    # возвращает количество товарных позиций
    return total_quantity(all_quantity)


# считает общее количество заказанной единицы товара и возвращает результат
def total_quantity(list_quantity):
    order_total_quantity = 0
    for item in list_quantity:
        order_total_quantity += item
    return order_total_quantity
