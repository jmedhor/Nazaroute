from sqlalchemy import Column, Integer, String, Float, Table, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

# Tabla intermedia ruta <-> punto
ruta_punto = Table(
    "ruta_punto",
    Base.metadata,
    Column("ruta_id", Integer, ForeignKey("rutas.id")),
    Column("punto_id", Integer, ForeignKey("puntos.id")),
)

class Punto(Base):
    __tablename__ = "puntos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    descripcion = Column(String, default="")
    latitud = Column(Float, nullable=False)
    longitud = Column(Float, nullable=False)

    rutas = relationship("Ruta", secondary=ruta_punto, back_populates="puntos")


class Ruta(Base):
    __tablename__ = "rutas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    descripcion = Column(String, default="")

    puntos = relationship("Punto", secondary=ruta_punto, back_populates="rutas")
