import flask_sqlalchemy
from flask_sqlalchemy import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Column,String,Integer,Float,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship,sessionmaker
import os
import cx_Oracle

base = declarative_base()

class instructor(base):
    __tablename__ = "<TABLENAME>"

    id = Column(Integer,primary_key = True)
    name = Column(String(100))
    dept_name = Column(String(150))
    salary = Column(Integer)
    
if __name__ == "__main__":

    engine = create_engine('oracle://<USER_NAME>:<Password>')
    base.metadata.create_all(engine)
    print("<TABLE> Created Successfully")

    Session = sessionmaker(engine)

    session = Session()
    user = instructor()
    user.id = <ID_NUM>
    user.name = <'NAME'>
    user.dept_name = <'DEPT_NAME'>
    user.salary = <SALARY>
    session.add(user)
    session.commit()
    session.close()
    
print("Record Inserted into <TABLENAME>")
    
