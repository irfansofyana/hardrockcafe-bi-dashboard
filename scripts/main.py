import os
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from scripts.schema.tables import Base, Customer, Cafe, Product, Promo, Time, Guest
from loader import load_cafes_table
from scripts.fake_data_generator.cafe import generate_fake_cafes

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

    fake_cafes = generate_fake_cafes()
    load_cafes_table(session, fake_cafes)
