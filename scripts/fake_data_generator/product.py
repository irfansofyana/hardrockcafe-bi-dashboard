# name, description, category_name, category_description, price_currency, price_amount
from faker import Faker
import random
import json


def generate_fake_products():
    def read_products_name(path, is_json=False):
        with open(path, 'r') as f:
            if is_json:
                products_name = json.load(f)
            else:
                products_name = f.read()
                products_name = products_name.split('\n')
        return products_name

    def generate_product(products, category):
        category_product_description = {
            'Foods': 'Foods that are available for dine-in and pick-up order',
            'Drinks': 'Drinks that are available for dine-in and pick-up order',
            'Snacks': 'Snack that are available for dine-in and pick-up order',
        }
        price_range = {
            'Foods': (20, 200),
            'Drinks': (10, 100),
            'Snacks': (15, 150),
        }

        generated_products = []
        for product in products:
            generated_product = {
                'name': product,
                'description': f'{product} is one of the best {category} produced by hard rock cafe',
                'category_name': category,
                'category_description': category_product_description[category],
                'price_currency': 'USD',
                'price_amount': random.randint(price_range[category][0], price_range[category][1])
            }
            generated_products.append(generated_product)

        return generated_products

    def generate_packages(packages, category):
        products = []
        for package in packages:
            product = {
                'name': package,
                'description': packages[package]['Description'],
                'category_name': f'{category} package',
                'category_description': f'Good {category} packages from Hard rock cafe',
                'price_currency': packages[package]['Currency'],
                'price_amount': packages[package]['Price']
            }
            products.append(product)

        return products

    foods_name_directory        = 'static/foods_name.txt'
    drinks_name_directory       = 'static/drinks_name.txt'
    snacks_name_directory       = 'static/snacks_name.txt'
    wedding_packages_directory  = 'static/wedding_packages.json'
    parties_events_directory    = 'static/party_event_packages.json'

    foods_name              = read_products_name(foods_name_directory)
    drinks_name             = read_products_name(drinks_name_directory)
    snacks_name             = read_products_name(snacks_name_directory)
    wedding_packages        = read_products_name(wedding_packages_directory, is_json=True)
    parties_events_packages = read_products_name(parties_events_directory, is_json=True)

    products = []
    products += generate_product(foods_name, 'Foods')
    products += generate_product(drinks_name, 'Drinks')
    products += generate_product(snacks_name, 'Snacks')
    products += generate_packages(wedding_packages, 'Wedding')
    products += generate_packages(parties_events_packages, 'Parties and Events')

    return products

