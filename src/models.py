from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship


db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(80), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(120),nullable=False)

    favoritos_personajes = db.relationship('')
    
    def serialize(self):
        return {
            "id": self.id,
            "username":self.username,
            "email": self.email,
            # do not serialize the password, its a security breach

        }

class Planets(db.Model):
    __tablename__="planets"

    id: Mapped[int] = mapped_column (primary_key=True, autoincrement=True)
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

    id: Mapped[int] = mapped_column (primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(80), unique=True, nullable=False)
    color_de_ojos: Mapped[str] = mapped_column(String(80), nullable=True)

    def serialize(self):
        return{
            "id": self.id,
            "name":self.name,
            "color_de_ojos": self.color_de_ojos
        }

class TablaIntermediaDePersonajesFavoritos(db.Model):
    __tablename__="tabla_intermedia_de_personajes_favoritos"

    user_id: Mapped[int] = mapped_column(db.ForeignKey('user.id'), primary_key=True)
    character_id: Mapped[int] = mapped_column(db.ForeignKey('characters.id', primary_key=True))

    def serialize(self):
        return{
            "user_id":self.user_id,
            "character_id":self.character_id,
        }

class TablaIntermediaDePlanetasFavoritos(db.Model):
    __tablename__="tabla_intermedia_de_planetas_favoritos"

    user_id: Mapped[int] = mapped_column(db.ForeignKey('user.id'), primary_key=True)
    planet_id: Mapped[int] = mapped_column(db.ForeignKey('planets.id', primary_key=True))

    def serialize(self):
        return{
            "user_id": self.user_id,
            "planet_id": self.planet_id,
        }