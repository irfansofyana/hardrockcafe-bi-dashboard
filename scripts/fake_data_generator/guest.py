# name, country_origin, performance_category, fee_rate_per_hour, fee_currency
from faker import Faker
import random

def generate_fake_guests():
    NUMBER_OF_GENERATED_GUESTS = 300
    composition = [
        int(NUMBER_OF_GENERATED_GUESTS / 2),
        int(NUMBER_OF_GENERATED_GUESTS / 9),
        int(NUMBER_OF_GENERATED_GUESTS / 10),
        int(NUMBER_OF_GENERATED_GUESTS / 17),
        int(NUMBER_OF_GENERATED_GUESTS / 19),
        int(NUMBER_OF_GENERATED_GUESTS / 20),
        int(NUMBER_OF_GENERATED_GUESTS / 30)
    ]
    remainder = NUMBER_OF_GENERATED_GUESTS - sum(composition)
    composition[0] += remainder

    performance_category_composition = {
        'Band: Genre Rock and Roll': composition[0],
        'Band: Genre Pop': composition[1],
        'Single: Genre Pop': composition[2],
        'Single: Genre RnB': composition[3],
        'Band: Genre Reggae': composition[4],
        'Single: Genre EDM': composition[5],
        'Band: Genre Jazz': composition[6]
    }

    fake = Faker()
    guests = []
    for category in performance_category_composition:
        for _ in range(performance_category_composition[category]):
            performance_category = category

            is_band = category.find(':') == 4
            name = 'The ' + fake.first_name() + ' And ' + fake.last_name() if is_band else fake.name()

            country_origin = fake.country()
            fee_rate_per_hour = random.randint(500, 5000)
            fee_currency = 'USD'

            guest = {
                'name': name,
                'country_origin': country_origin,
                'performance_category': performance_category,
                'fee_rate_per_hour': fee_rate_per_hour,
                'fee_currency': fee_currency
            }

            guests.append(guest)

    return guests




