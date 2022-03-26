
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import urllib
from databases import Database

SQLALCHEMY_DATABASE_URL  = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
Base=declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
database=Database(SQLALCHEMY_DATABASE_URL)