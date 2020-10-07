from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key = True, nullable = False, autoincrement = True)
    name = Column(String(10), unique = True, nullable = False)
    userid = Column(String(10), nullable = False)
    password = Column(String(10), nullable = False)

    def __init__(self, name, userid, password):
        self.name = name
        self.userid = userid
        self.password = password
    def __repr__(self):
        return "<User('%s', '%s', '%s')>" % (self.name, self.userid, self.password)

if __name__ == '__main__':
    user = User('test', 'test', 'test')
    user.name        # 'haruair'
    user.userid    # '1234'
    user.password    # '1234'
    
    print(user.__repr__)