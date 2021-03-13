import os
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base


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


Base = declarative_base()


class TestTable(Base):
    __tablename__ = 'test_table'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    test_name = Column(String(20))
    description = Column(String(20))


# TODO: Create the real tables using mapper

if __name__=="__main__":
    env_var = get_env()

    mysql_engine = create_mysql_engine(env_var['mysql_connection_string'])
    session = create_session(mysql_engine)

    Base.metadata.create_all(mysql_engine)

    ex_row = TestTable(test_name='test_01', description='this_is_only_testing_01')
    session.add(ex_row)
    session.commit()

    for row in session.query(TestTable).order_by(TestTable.id):
        print(row.id, row.test_name, row.description)
