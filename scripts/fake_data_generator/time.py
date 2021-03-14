# date, minute, hour, day_name, month, year, holiday_status, weekend_status, weekday_status
import datetime
import random


def generate_fake_dates():
    def generate_random_date_between(s_date, e_date):
        time_between_dates = e_date - s_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)

        return s_date + datetime.timedelta(days=random_number_of_days)

    def is_weekend(name_of_day):
        weekend_days = ['saturday', 'sunday']

        return name_of_day.lower() in weekend_days

    dates = []
    NUMBER_OF_GENERATED_DATES = 10000

    for _ in range(NUMBER_OF_GENERATED_DATES):
        start_date = datetime.date(2019, 1, 1)
        end_date = datetime.date(2021, 3, 16)
        random_date = generate_random_date_between(start_date, end_date)

        minute_1 = random.randint(0, 59)
        hour_1 = random.randint(11, 19)
        minute_2 = random.randint(0, 59)
        hour_2 = random.randint(hour_1 + 1, hour_1 + 3)

        day_name = random_date.strftime("%A")
        month = random_date.day
        year = random_date.year

        holiday_status = True if (random.randint(0, 1) == 0) else False
        weekend_status = is_weekend(day_name)
        weekday_status = not weekend_status

        common_data = {
            'date': str(random_date),
            'day_name': day_name,
            'month': month,
            'year': year,
            'holiday_status': holiday_status,
            'weekend_status': weekend_status,
            'weekday_status': weekday_status
        }

        date_1 = {
            'minute': minute_1,
            'hour': hour_1,
        }

        date_2 = {
            'minute': minute_2,
            'hour': hour_2,
        }

        dates.append({**common_data, **date_1})
        dates.append({**common_data, **date_2})

    return dates
