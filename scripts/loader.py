from scripts.schema.tables import Customer, Cafe, Product, Promo, Time, Guest, LivePerformance, Sales

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

def load_live_performance_table(session, live_performances):
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
        session.add(row)
    session.commit()

def load_promo_table(session, promos):
    for promo in promos:
        row = Promo(
            name                    = promo['name'],
            description             = promo['description'],
            started_date            = promo['started_date'],
            ended_date              = promo['ended_date'],
            category_name           = promo['category_name'],
            category_description    = promo['category_description'],
            currency_used           = promo['currency_used'],
            max_promo_amount        = promo['max_promo_amount']
        )
        session.add(row)
    session.commit()

def load_sales_table(session, sales):
    for sale in sales:
        row = Sales(
            cafe_id         =   sale['cafe_id'],
            product_id      =   sale['product_id'],
            time_id         =   sale['time_id'],
            customer_id     =   sale['customer_id'],
            promo_id        =   sale['promo_id'],
            total_quantity  =   sale['total_quantity'],
            payment_currency=   sale['payment_currency'],
            gross_payment   =   sale['gross_payment'],
            total_discount  =   sale['total_discount'],
            total_payment   =   sale['total_payment']
        )
        session.add(row)
    session.commit()
