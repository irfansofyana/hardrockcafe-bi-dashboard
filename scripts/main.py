import os
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from scripts.schema.tables import Base
from loader import load_cafe_table, load_customer_table, load_guest_table, load_time_table, load_product_table, load_live_performance_table
from scripts.fake_data_generator.cafe import generate_fake_cafes
from scripts.fake_data_generator.guest import generate_fake_guests
from scripts.fake_data_generator.product import generate_fake_products
from scripts.fake_data_generator.time import generate_fake_times
from scripts.fake_data_generator.customer import generate_fake_customers
from scripts.fake_data_generator.live_performance import generate_fake_live_performance

def get_env():
    load_dotenv()

    mysql_connection_string = os.getenv('MYSQL_CONNECTION_STRING')

    data = {
        'mysql_connection_string': mysql_connection_string
    }
    return data


def create_mysql_engine(mysql_connection_string):
    try:
        mysql_engine = create_engine(mysql_connection_string)
        return mysql_engine
    except Exception as err:
        print('Error: ', err)


def create_session(engine):
    try:
        Session = sessionmaker(bind=engine)
        session = Session()
        return session
    except Exception as err:
        print('Error: ', err)


if __name__=="__main__":
    env_var = get_env()

    mysql_engine = create_mysql_engine(env_var['mysql_connection_string'])
    session = create_session(mysql_engine)

    Base.metadata.create_all(mysql_engine)

    try:
        fake_cafes = generate_fake_cafes()
        load_cafe_table(session, fake_cafes)
        print('Cafe table loaded!')

        fake_customers = generate_fake_customers()
        load_customer_table(session, fake_customers)
        print('Customer table loaded!')

        fake_times = generate_fake_times()
        load_time_table(session, fake_times)
        print('Time table loaded!')

        fake_guests = generate_fake_guests()
        load_guest_table(session, fake_guests)
        print('Guest table loaded!')

        fake_products = generate_fake_products()
        load_product_table(session, fake_products)
        print('Product table loaded!')

        fake_live_performances = generate_fake_live_performance(fake_cafes, fake_guests, fake_times)
        load_live_performance_table(session, fake_live_performances)
        print('Live performance loaded!')

    except Exception as err:
        print(err)
