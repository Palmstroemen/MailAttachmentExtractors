__author__ = 'oliver'
# coding=utf-8

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://oliver:revillo@localhost:5432/oliver')
#engine = create_engine('postgresql://clixpi:cflpi9xde4cfu8r5e4@localhost/checkthis')
#engine = create_engine('sqlite:///:memory:')   # das wäre in In-Memory-Datenbank
#engine = create_engine('sqlite:///Database.db', echo=False)
Session = sessionmaker(bind=engine)

Base = declarative_base()