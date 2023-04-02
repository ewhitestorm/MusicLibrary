from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Text, DateTime, MetaData
#from .sqlalchemy_db import EngineSqlAlchemy


Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column('id', Integer, primary_key=True)	
    username = Column('username', Text)			        
    date = Column('date', Text)

# Base.metadata.create_all(EngineSqlAlchemy.engine)
