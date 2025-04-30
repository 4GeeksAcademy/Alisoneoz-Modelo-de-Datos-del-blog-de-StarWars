from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column('userID',primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(80), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(120),nullable=False)
    
    def serialize(self):
        return {
            "id": self.id,
            "username":self.username,
            "email": self.email,
            # do not serialize the password, its a security breach

        }

class Planets(db.Model):
    __tablename__="planets"

    id: Mapped[int] = mapped_column ('planetID', primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(80), unique=True, nullable=False)
    clima: Mapped[str] = mapped_column(String(80), nullable=True)

    def serialize(self):
        return{
            "id": self.id,
            "name":self.name,
            "clima": self.clima
        }

class Characters(db.Model):
    __tablename__="characters"

    id: Mapped[int] = mapped_column ('characterID', primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(80), unique=True, nullable=False)
    color_de_ojos: Mapped[str] = mapped_column(String(80), nullable=True)

    def serialize(self):
        return{
            "id": self.id,
            "name":self.name,
            "color_de_ojos": self.color_de_ojos
        }
