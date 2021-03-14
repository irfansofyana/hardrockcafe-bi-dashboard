# name, capacity, address, city, state, zip_code, country
from faker import Faker
import json
import random

def generate_fake_cafes():
    with open('list_countries_cities_hardrockcafe.json', 'r') as f:
        countries_cities_mapper = json.load(f)

    fake = Faker()
    cafes = []

    for country in countries_cities_mapper:
        for city in countries_cities_mapper[country]:
            name        = 'Hard Rock Cafe ' + city
            capacity    = random.randint(100, 200)
            address     = city + ' street number ' + str(random.randint(1, 300))
            state       = city + ' state'
            zip_code    = fake.zipcode()

            cafe = {
                'name': name,
                'capacity': capacity,
                'address': address,
                'city': city,
                'state': state,
                'zip_code': zip_code,
                'country': country
            }

            cafes.append(cafe)

    return cafes