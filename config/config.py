from sqlalchemy import  create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

connection = "mysql+pymysql://root:root@localhost:3306/gestor_turnos"

engine = create_engine(connection, echo=True) 

localSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()