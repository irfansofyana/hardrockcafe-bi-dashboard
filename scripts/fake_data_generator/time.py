# date, minute, hour, day_name, month, year, holiday_status, weekend_status, weekday_status
import datetime
import random


def generate_fake_times():
    def is_weekend(name_of_day):
        weekend_days = ['saturday', 'sunday']

        return name_of_day.lower() in weekend_days

    dates = []

    date_iterator = datetime.date(2018, 1, 1)
    while date_iterator != datetime.date.today():
        day_name = date_iterator.strftime("%A")
        month = date_iterator.month
        year = date_iterator.year
        weekend_status = is_weekend(day_name)
        weekday_status = not weekend_status
        if weekend_status:
            holiday_status = True
        elif random.randint(0, 18) == 0:  # Assumption the probability of holiday in a year is 1/18
            holiday_status = True
        else:
            holiday_status = False

        for hour in range(11, 21):
            next_one_hour = hour + 1

            date = {
                'date': str(date_iterator),
                'day_name': day_name,
                'month': month,
                'year': year,
                'holiday_status': holiday_status,
                'weekend_status': weekend_status,
                'weekday_status': weekday_status,
                'minute': 0
            }

            dates.append({**date, **{'hour': hour}})
            dates.append({**date, **{'hour': next_one_hour}})

        date_iterator = date_iterator + datetime.timedelta(days=1)

    return dates
