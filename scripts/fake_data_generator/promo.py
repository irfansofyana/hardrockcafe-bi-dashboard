# name, description, started_date, ended_date, category_name, description, currency_used, max_promo_amount
import random
import datetime
from faker import Faker

def generate_fake_promos():
    def generate_random_date_between(s_date, e_date):
        time_between_dates = e_date - s_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)

        return s_date + datetime.timedelta(days=random_number_of_days)

    NUMBER_OF_GENERATED_PROMOS = 300
    promo_category = {
        'Buy one get one': 'You buy one actually get two',
        'Free delivery': 'You dont have to pay the delivery fee',
        'Discount 30%': 'You only pay 70% from the original price',
        'Discount 50%': 'You onlu pay 50% from the original price',
        'Discount 100%': 'FREEE for you!!!',
        'Special Day': 'Today is special day! Get your food with cheaper price'
    }
    number_of_promo_category = len(list(promo_category.values()))
    promo_category_list = list(promo_category.keys())

    long_time_ago = datetime.date(2018, 1, 1)
    now_time      = datetime.date.today()

    fake = Faker()
    generated_promos = []

    for i in range(NUMBER_OF_GENERATED_PROMOS):
        started_date    = generate_random_date_between(long_time_ago, now_time)
        ended_date      = started_date + datetime.timedelta(days=random.randint(1, 5))
        name            = fake.word() + " promo"
        description     = "Legit promo only for you"
        chosen_category = random.randint(0, number_of_promo_category-1)
        category_name   = promo_category[promo_category_list[chosen_category]]
        currency_used   = 'USD'
        max_promo_amount = random.randint(5, 20)

        promo = {
            'name': name,
            'description': description,
            'started_date':str(started_date),
            'ended_date': str(ended_date),
            'category_name': category_name,
            'currency_used': currency_used,
            'max_promo_amount': max_promo_amount
        }

        generated_promos.append(promo)

    return generated_promos
