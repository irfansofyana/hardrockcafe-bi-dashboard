import random

def generate_fake_sales(cafes, products, times, customers, promos):
    def add_atribute_id(list):
        for order, element in enumerate(list):
            element['id'] = order + 1
        return list

    cafes       = add_atribute_id(cafes)
    products    = add_atribute_id(products)
    customers   = add_atribute_id(customers)
    promos      = add_atribute_id(promos)

    generated_data = []

    return generated_data
