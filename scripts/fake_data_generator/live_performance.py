import random

def generate_fake_live_performance(cafes, guests, times):
    def get_times_attribute(times_len):
        # start index: 1 mod 11
        max_group = (times_len - 1) // 11

        chosen_group = 11 * random.randint(0, max_group) + 1

        start_time = random.randint(chosen_group, chosen_group + 8)
        end_time   = random.randint(start_time + 1, min(chosen_group + 9, start_time + 3))

        return start_time, end_time

    def filter_guest_by_category(guests, category):
        return list(filter(lambda guest: guest['performance_category'] == category, guests))

    def get_number_of_visitors(low, high):
        number_of_visitors_range = [
            (30, 50),  # low
            (51, 100), # low medium
            (101, 150), # medium
            (151, 300), # medium-high
            (301, 500)  # high
        ]
        chosen = random.randint(low, high)
        range_chosen = number_of_visitors_range[chosen]
        return random.randint(range_chosen[0], range_chosen[1])

    def get_time_differences_in_minute(times, start, end):
        start_time = times[start]
        end_time   = times[end]
        if (start_time['hour'] > end_time['hour']):
            print('bug')
            print(start_time)
            print(end_time)

        return 60 * (end_time['hour'] - start_time['hour'])

    def gather_data(
            cafe_id, guest_id, start_time_id, end_time_id,
            number_of_visitors, number_of_orders, performance_duration_in_minute
    ):
        return {
            'cafe_id': cafe_id,
            'guest_id': guest_id,
            'start_time_id': start_time_id,
            'end_time_id': end_time_id,
            'number_of_visitors': number_of_visitors,
            'number_of_orders': number_of_orders,
            'performance_duration_in_minute': performance_duration_in_minute
        }
    def add_atribute_id(list):
        for order, element in enumerate(list):
            element['id'] = order + 1
        return list


    cafes   = add_atribute_id(cafes)
    guests  = add_atribute_id(guests)
    times   = add_atribute_id(times)

    performance_category = [
        'Band: Genre Rock and Roll',
        'Band: Genre Pop',
        'Single: Genre Pop',
        'Single: Genre RnB',
        'Band: Genre Reggae',
        'Single: Genre EDM',
        'Band: Genre Jazz'
    ]
    filtered_guests = []
    for category in performance_category:
        filtered_guests += filter_guest_by_category(guests, category)

    generated_data = []
    for i, cafe in enumerate(cafes):
        frequency = random.randint(40, 60)

        detail_freq = [None] * 7
        detail_freq[0]    = int(frequency * random.randint(30, 35) / 100) #band_rock
        detail_freq[1]    = int(frequency * random.randint(20, 20) / 100) #band_pop
        detail_freq[2]    = int(frequency * random.randint(10, 16) / 100) #single_pop
        detail_freq[3]    = int(frequency * random.randint(10, 12) / 100) #single_rnb
        detail_freq[4]    = int(frequency * random.randint(5, 7) / 100)   #band_reggae
        detail_freq[5]    = int(frequency * random.randint(1, 5) / 100)   #single_edm
        detail_freq[6]    = int(frequency * random.randint(1, 5) / 100)   #band_jazz
        remainder_freq    = 100 - sum(detail_freq)
        detail_freq[0] += remainder_freq

        number_of_visitors_freq = [
            (3, 4),
            (3, 3),
            (2, 3),
            (2, 2),
            (1, 3),
            (1, 2),
            (1, 1)
        ]

        cafe_id = i + 1
        times_len = len(times)
        for category_order in range(7):
            for _ in range(detail_freq[category_order]):
                chosen_guest = random.randint(0, len(filtered_guests[category_order]))
                guest_id = filtered_guests[chosen_guest]['id']
                start_time, end_time = get_times_attribute(times_len)
                number_of_visitors = get_number_of_visitors(
                    number_of_visitors_freq[category_order][0],
                    number_of_visitors_freq[category_order][1]
                )
                number_of_orders = random.randint(number_of_visitors, number_of_visitors * 2)
                performance_duration_in_minute = get_time_differences_in_minute(times, start_time, end_time)

                generated_data.append(gather_data(
                    cafe_id, guest_id, start_time, end_time,
                    number_of_visitors, number_of_orders, performance_duration_in_minute
                ))

    return generated_data
