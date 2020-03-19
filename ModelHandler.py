from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///Model.db', echo=True)


def make_session():
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def return_connection():  # return a connection to execute raw SQL
    conn = engine.connect()
    return conn


def return_meta():
    return Base.metadata
