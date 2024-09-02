from sqlalchemy import Column, Integer, String, Date, ForeignKey, Boolean, DateTime
import datetime

from models import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(25), nullable=False)
    password = Column(String(100), nullable=False)
    email = Column(String(25), nullable=False)
    first_name = Column(String(25), nullable=False)
    last_name = Column(String(25), nullable=False)
    is_admin = Column(Boolean, default=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.first_name}', '{self.last_name}', '{self.country}', '{self.is_admin}')"

class TokenTable(Base):
    __tablename__ = "user_tokens"
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    access_token = Column(String(450), primary_key=True)
    refresh_token = Column(String(450),nullable=False)
    status = Column(Boolean)
    created_date = Column(DateTime, default=datetime.datetime.now)