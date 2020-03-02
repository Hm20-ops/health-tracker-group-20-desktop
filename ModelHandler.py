from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
engine = create_engine('sqlite:///Model.db', echo=True)

def make_session():
    Session = sessionmaker(bind=engine)
    session = Session()
    return session
