from scripts.schema.tables import Customer, Cafe, Product, Promo, Time, Guest, LivePerformance

def load_cafe_table(session, cafes):
    for cafe in cafes:
        row = Cafe (
            name        = cafe['name'],
            capacity    = cafe['capacity'],
            address     = cafe['address'],
            city        = cafe['city'],
            state       = cafe['state'],
            zip_code    = cafe['zip_code'],
            country     = cafe['country']
        )
        session.add(row)
    session.commit()

def load_customer_table(session, customers):
    for customer in customers:
        row = Customer(
            first_name  = customer['first_name'],
            last_name   = customer['last_name'],
            email       = customer['email'],
            phone_number= customer['phone_number'],
            address     = customer['address']
        )
        session.add(row)
    session.commit()

def load_guest_table(session, guests):
    for guest in guests:
        row = Guest(
            name                = guest['name'],
            country_origin      = guest['country_origin'],
            performance_category= guest['performance_category'],
            fee_currency        = guest['fee_currency'],
            fee_rate_per_hour   = guest['fee_rate_per_hour']
        )
        session.add(row)
    session.commit()

def load_time_table(session, times):
    for time in times:
        row = Time(
            date            = time['date'],
            minute          = time['minute'],
            hour            = time['hour'],
            day_name        = time['day_name'],
            month           = time['month'],
            year            = time['year'],
            holiday_status  = time['holiday_status'],
            weekend_status  = time['weekend_status'],
            weekday_status  = time['weekday_status']
        )
        session.add(row)
    session.commit()

def load_product_table(session, products):
    for product in products:
        row = Product(
            name                    = product['name'],
            description             = product['description'],
            category_name           = product['category_name'],
            category_description    = product['category_description'],
            price_currency          = product['price_currency'],
            price_amount            = product['price_amount']
        )
        session.add(row)
    session.commit()

def load_live_performance_table(sesion, live_performances):
    for live_performance in live_performances:
        row = LivePerformance(
            cafe_id                         = live_performance['cafe_id'],
            guest_id                        = live_performance['guest_id'],
            start_time_id                   = live_performance['start_time_id'],
            end_time_id                     = live_performance['end_time_id'],
            number_of_visitors              = live_performance['number_of_visitors'],
            number_of_orders                = live_performance['number_of_orders'],
            performance_duration_in_minute  = live_performance['performance_duration_in_minute']
        )
        sesion.add(row)
    sesion.commit()