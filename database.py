
from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker 
from sqlalchemy import create_engine 
import atexit 

PG_DSN = 'postgresql://nikolay:310585@127.0.0.1:5431/flask_advertisement' 
engine = create_engine(PG_DSN) 
Base = declarative_base() 

class AdvertisementModel(Base):
  
  __tablename__ = 'advertisement'

  id = Column(Integer, primary_key=True, autoincrement=True)
  title = Column(String, unique=True, nullable=False, index=True)
  description = Column(String, nullable=False)
  create_time = Column(DateTime, server_default=func.now()) 
  owner = Column(String, unique=True, nullable=False, index=True)

Base.metadata.create_all(engine) 
Session = sessionmaker(bind=engine) 

atexit.register(engine.dispose) 

  





