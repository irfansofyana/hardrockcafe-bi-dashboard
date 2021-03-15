from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence, Text, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class Customer(Base):
    __tablename__   = 'customer'

    id              = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    first_name      = Column(String(50), nullable=False)
    last_name       = Column(String(50))
    email           = Column(String(50), nullable=False)
    phone_number    = Column(String(30))
    address         = Column(String(100))

    sales_customer   = relationship("Sales", back_populates="customer_sales")


class Cafe(Base):
    __tablename__       = 'cafe'

    id                  = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name                = Column(String(50), nullable=False)
    capacity            = Column(Integer, nullable=False)
    address             = Column(String(100), nullable=False)
    city                = Column(String(50), nullable=False)
    state               = Column(String(50), nullable=False)
    zip_code            = Column(String(10), nullable=False)
    country             = Column(String(50), nullable=False)

    cafe_performance    = relationship("LivePerformance", back_populates="cafe_relation")
    sales_cafe          = relationship("Sales", back_populates="cafe_sales")


class Product(Base):
    __tablename__           = 'product'

    id                      = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name                    = Column(String(50), nullable=False)
    description             = Column(Text)
    category_name           = Column(String(50), nullable=False)
    category_description    = Column(Text)
    price_currency          = Column(String(5), nullable=False)
    price_amount            = Column(Integer, nullable=False)

    sales_product           = relationship("Sales", back_populates="product_sales")

class Promo(Base):
    __tablename__           = 'promo'

    id                      = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name                    = Column(String(50), nullable=False)
    description             = Column(Text)
    started_date            = Column(Date)
    ended_date              = Column(Date)
    category_name           = Column(String(50))
    category_description    = Column(Text)
    currency_used           = Column(String(5))
    max_promo_amount        = Column(Integer)

    sales_promo      = relationship("Sales", back_populates="promo_sales")


class Time(Base):
    __tablename__           = 'time'

    id                      = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    date                    = Column(Date, nullable=False)
    minute                  = Column(Integer)
    hour                    = Column(Integer)
    day_name                = Column(String(20), nullable=False)
    month                   = Column(Integer, nullable=False)
    year                    = Column(Integer, nullable=False)
    holiday_status          = Column(Boolean, nullable=False)
    weekend_status          = Column(Boolean, nullable=False)
    weekday_status          = Column(Boolean, nullable=False)

    sales_time              = relationship("Sales", back_populates="time_sales")


class Guest(Base):
    __tablename__           = 'guest'

    id                      = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name                    = Column(String(50), nullable=False)
    country_origin          = Column(String(100), nullable=False)
    performance_category    = Column(String(100), nullable=False)
    fee_currency            = Column(String(5), nullable=False)
    fee_rate_per_hour       = Column(Integer, nullable=False)

    guest_performance       = relationship("LivePerformance", back_populates="guest_relation")


class LivePerformance(Base):
    __tablename__                          = 'live_performance'

    id                                     = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    cafe_id                                = Column(Integer, ForeignKey('cafe.id'))
    guest_id                               = Column(Integer, ForeignKey('guest.id'))
    start_time_id                          = Column(Integer, ForeignKey('time.id'))
    end_time_id                            = Column(Integer, ForeignKey('time.id'))

    number_of_visitors                     = Column(Integer, nullable=False)
    number_of_orders                       = Column(Integer, nullable=False)
    performance_duration_in_minute         = Column(Integer, nullable=False)

    cafe_relation                          = relationship("Cafe", back_populates="cafe_performance")
    guest_relation                         = relationship("Guest", back_populates="guest_performance")
    start_time_relation                    = relationship("Time", foreign_keys=[start_time_id])
    end_time_relation                      = relationship("Time", foreign_keys=[end_time_id])

class Sales(Base):
    __tablename__       = 'sales'

    id                  = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    cafe_id             = Column(Integer, ForeignKey('cafe.id'))
    product_id          = Column(Integer, ForeignKey('product.id'))
    time_id             = Column(Integer, ForeignKey('time.id'))
    customer_id         = Column(Integer, ForeignKey('customer.id'))
    promo_id            = Column(Integer, ForeignKey('promo.id'))

    total_quantity      = Column(Integer, nullable=False)
    payment_currency    = Column(String(5), nullable=False)
    gross_payment       = Column(Integer, nullable=False)
    total_discount      = Column(Integer, nullable=False)
    total_payment       = Column(Integer, nullable=False)

    cafe_sales       = relationship("Cafe", back_populates="sales_cafe")
    product_sales    = relationship("Product", back_populates="sales_product")
    time_sales       = relationship("Time", back_populates="sales_time")
    customer_sales   = relationship("Customer", back_populates="sales_customer")
    promo_sales      = relationship("Promo", back_populates="sales_promo")
