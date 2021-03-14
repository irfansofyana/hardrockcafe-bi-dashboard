from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence, Text, Date, Boolean

Base = declarative_base()

class Customer(Base):
    __tablename__   = 'customer'

    id              = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    first_name      = Column(String(15), nullable=False)
    last_name       = Column(String(30))
    email           = Column(String(50), nullable=False)
    phone_number    = Column(String(30))
    address         = Column(String(30))

class Cafe(Base):
    __tablename__   = 'cafe'

    id              = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name            = Column(String(50), nullable=False)
    capacity        = Column(Integer, nullable=False)
    address         = Column(String(100), nullable=False)
    city            = Column(String(20), nullable=False)
    state           = Column(String(20), nullable=False)
    zip_code        = Column(String(10), nullable=False)
    country         = Column(String(20), nullable=False)

class Product(Base):
    __tablename__           = 'product'

    id                      = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name                    = Column(String(50), nullable=False)
    description             = Column(Text)
    category                = Column(String(20), nullable=False)
    category_description    = Column(Text)
    price_currency          = Column(String(5), nullable=False)
    price_amount            = Column(Integer, nullable=False)

class Promo(Base):
    __tablename__           = 'promo'

    id                      = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name                    = Column(String(20), nullable=False)
    description             = Column(Text)
    started_date            = Column(Date, nullable=False)
    ended_date              = Column(Date, nullable=False)
    category_name           = Column(String(50), nullable=False)
    category_description    = Column(Text)
    currency_used           = Column(String(5))
    max_promo_amount        = Column(Integer)

class Time(Base):
    __tablename__           = 'time'

    id                      = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    date                    = Column(Date, nullable=False)
    minute                  = Column(Integer)
    hour                    = Column(Integer)
    day_name                = Column(String(10), nullable=False)
    month                   = Column(Integer, nullable=False)
    year                    = Column(Integer, nullable=False)
    holiday_status          = Column(Boolean, nullable=False)
    weekend_status          = Column(Boolean, nullable=False)
    weekday_status          = Column(Boolean, nullable=False)

class Guest(Base):
    __tablename__           = 'guest'

    id                      = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name                    = Column(String(20), nullable=False)
    country_origin          = Column(String(20), nullable=False)
    performance_category    = Column(String(20), nullable=False)
    fee_currency            = Column(String(5), nullable=False)
    fee_rate_per_hour       = Column(Integer, nullable=False)