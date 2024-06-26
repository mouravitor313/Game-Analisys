from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from database import Base
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    rule = Column(String, index=True)
    password_hash = Column(String)
    is_active = Column(Boolean)
    role = Column(String)

    def set_password(self, password):
        self.password_hash = pwd_context.hash(password)

    def check_password(self, password):
        return pwd_context.verify(password, self.password_hash)

class Game(Base):
    __tablename__ = 'games'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    platform = Column(String)
    completed = Column(Boolean, default=False)
    complete_time = Column(Float, default=0.0)
    user_id = Column(Integer, ForeignKey("users.id"))

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "platform": self.platform,
            "completed": self.completed,
            "complete_time": self.complete_time,
            "user_id": self.user_id
        }
