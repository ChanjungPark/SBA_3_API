from sqlalchemy import create_engine

engine = create_engine('sqlite://')

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Integer, String

class Message(Base):
    __tablename__ = 'messages'
    
    id = Column(Integer, primary_key=True)
    message = Column(String)

Base.metadata.create_all(engine)
message = Message(message="Hello World!")
message.message # 'Hello World!

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

session.add(message)
session.commit()

query = session.query(Message)
instance = query.first()
print (instance.message) # Hello World!