import random

def generate_fake_sales(cafes, products, times, customers, promos):
    def add_atribute_id(list):
        for order, element in enumerate(list):
            element['id'] = order + 1
        return list

    def filter_product_by_category(products, category):
        return list(filter(lambda product: product['category_name'] == category, products))

    def random_total_quantity(category):
        if (category == 0):
            return random.randint(1, 3)
        elif (category == 1 or category == 2):
            return random.randint(1, 2)
        else:
            return 1

    def gather_date(
         cafe_id, product_id, time_id, customer_id, promo_id,
         total_quantity, payment_currency, gross_payment, total_discount,
         total_payment
    ):
        return {
            'cafe_id': cafe_id,
            'product_id': product_id,
            'time_id': time_id,
            'customer_id': customer_id,
            'promo_id': promo_id,
            'total_quantity': total_quantity,
            'payment_currency': payment_currency,
            'gross_payment': gross_payment,
            'total_discount': total_discount,
            'total_payment': total_payment
        }

    def get_random_food(foods, freq):
        number_of_foods = len(foods)
        fav_percentage = [0] * 3
        fav_percentage[0]  = int(freq * 45 / 100)
        fav_percentage[1]  = int(freq * 30 / 100)
        fav_percentage[2]  = int(freq * 15 / 100)
        remainder_freq  = freq - sum(fav_percentage)

        food_product_ids = []
        for id in range(3):
            food_product_ids += [id+1 for _ in range(fav_percentage[id])]
        for _ in range(remainder_freq):
            chosen_id = random.randint(4, number_of_foods)
            food_product_ids.append(chosen_id)
        return food_product_ids

    def get_random_drink(drinks, freq):
        number_of_drinks = len(drinks)
        fav_percentage = [0] * 3
        fav_percentage[0] = int(freq * 30 / 100)
        fav_percentage[1] = int(freq * 45 / 100)
        fav_percentage[2] = int(freq * 20 / 100)
        remainder_freq = freq - sum(fav_percentage)

        drink_product_ids = []
        for id in range(3):
            drink_product_ids += [id + 1 for _ in range(fav_percentage[id])]
        for _ in range(remainder_freq):
            chosen_id = random.randint(4, number_of_drinks)
            drink_product_ids.append(chosen_id)
        return drink_product_ids

    def get_random_snack(snacks, freq):
        number_of_snacks = len(snacks)
        fav_percentage = [0] * 3
        fav_percentage[0] = int(freq * 45 / 100)
        fav_percentage[1] = int(freq * 15 / 100)
        fav_percentage[2] = int(freq * 30 / 100)
        remainder_freq = freq - sum(fav_percentage)

        snack_product_ids = []
        for id in range(3):
            snack_product_ids += [id + 1 for _ in range(fav_percentage[id])]
        for _ in range(remainder_freq):
            chosen_id = random.randint(4, number_of_snacks)
            snack_product_ids.append(chosen_id)
        return snack_product_ids

    def get_random_wedding(weddings, freq):
        number_of_weddings = len(weddings)
        fav_percentage = [0] * 3
        fav_percentage[0] = int(freq * 30 / 100)
        fav_percentage[1] = int(freq * 45 / 100)
        fav_percentage[2] = int(freq * 15 / 100)
        remainder_freq = freq - sum(fav_percentage)

        wedding_product_ids = []
        for id in range(3):
            wedding_product_ids += [id + 1 for _ in range(fav_percentage[id])]
        for _ in range(remainder_freq):
            chosen_id = random.randint(4, number_of_weddings)
            wedding_product_ids.append(chosen_id)
        return wedding_product_ids

    def get_random_party(parties, freq):
        number_of_parties = len(parties)
        fav_percentage = [0] * 3
        fav_percentage[0] = int(freq * 20 / 100)
        fav_percentage[1] = int(freq * 30 / 100)
        fav_percentage[2] = int(freq * 55 / 100)
        remainder_freq = freq - sum(fav_percentage)

        party_product_ids = []
        for id in range(3):
            party_product_ids += [id + 1 for _ in range(fav_percentage[id])]
        for _ in range(remainder_freq):
            chosen_id = random.randint(4, number_of_parties)
            party_product_ids.append(chosen_id)
        return party_product_ids

    cafes       = add_atribute_id(cafes)
    products    = add_atribute_id(products)
    customers   = add_atribute_id(customers)
    promos      = add_atribute_id(promos)
    times       = add_atribute_id(times)

    number_of_customers = len(customers)
    number_of_promos    = len(promos)
    number_of_times     = len(times)

    product_category = [
        'Foods',
        'Drinks',
        'Snacks',
        'Wedding package',
        'Parties and Events package'
    ]
    filtered_products = []
    for category in product_category:
        filtered_products += filter_product_by_category(products, category)

    generated_data = []
    for i, cafe in enumerate(cafes):
        frequency = random.randint(200, 300)

        detail_freq = [0] * 5
        detail_freq[0]  = int(frequency * random.randint(40, 50) / 100) # Foods
        detail_freq[1]  = int(frequency * random.randint(20, 25) / 100) # Drinks
        detail_freq[2]  = int(frequency * random.randint(10, 15) / 100) # Snacks
        detail_freq[3]  = int(frequency * random.randint(4, 6) / 100) # wedding
        detail_freq[4]  = int(frequency * random.randint(3, 4) / 100) # parties
        remainder_freq  = 100 - sum(detail_freq)
        detail_freq[0]  += remainder_freq

        cafe_id = i + 1
        for category_order in range(5):
            if (category_order == 0):
                product_ids = get_random_food(filtered_products[0], detail_freq[0])
            elif (category_order == 1):
                product_ids = get_random_drink(filtered_products[1], detail_freq[1])
            elif (category_order == 2):
                product_ids = get_random_snack(filtered_products[2], detail_freq[2])
            elif (category_order == 3):
                product_ids = get_random_wedding(filtered_products[3], detail_freq[3])
            else:
                product_ids = get_random_party(filtered_products[4], detail_freq[4])

            for product_id in product_ids:
                customer_id = random.randint(1, number_of_customers)
                promo_id   = random.randint(1, number_of_promos - 1)
                time_id     = random.randint(1, number_of_times)
                total_quantity = random_total_quantity(category_order)
                payment_currency = 'USD'
                gross_payment    = total_quantity * products[product_id - 1]['price_amount']
                is_discount     = random.randint(0, 9)
                if (is_discount == 1):
                    total_discount  = random.randint(1, promos[promo_id - 1]['max_promo_amount'])
                else:
                    total_discount  = 0
                    promo_id = number_of_promos
                total_payment = gross_payment - total_discount

                generated_data.append(gather_date (
                     cafe_id, product_id, time_id, customer_id, promo_id,
                     total_quantity, payment_currency, gross_payment, total_discount,
                     total_payment
                ))

    return generated_data
