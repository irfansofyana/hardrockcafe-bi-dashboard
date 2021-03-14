# First name, last name, email, phone number, address
from faker import Faker
import random


def generate_fake_customers():
    def get_domain_email(email):
        return email[email.find('@'):]

    customers = []
    locales = {
        0: 'en_US',
        1: 'en_AU',
        2: 'en_GB',
        3: 'id_ID',
        4: 'sk_SK',
        5: 'ru_RU'
    }
    fake = Faker(list(locales.values()))
    NUMBER_OF_GENERATED_CUSTOMERS = 10000

    for _ in range(NUMBER_OF_GENERATED_CUSTOMERS):
        choosen_locale = random.randint(0, 5)
        fake_choosen    = fake[locales[choosen_locale]]

        first_name      = fake_choosen.first_name()
        last_name       = fake_choosen.last_name()
        email           = first_name.lower() + last_name.lower() + get_domain_email(fake_choosen.ascii_email())
        phone_number    = fake_choosen.phone_number()
        address         = fake_choosen.address()

        customer = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'phone_number': phone_number,
            'address': address
        }
        customers.append(customer)

    return customers