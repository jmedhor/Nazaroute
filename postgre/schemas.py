from pydantic import BaseModel
from typing import List

class PuntoBase(BaseModel):
    nombre: str
    descripcion: str = ""
    latitud: float
    longitud: float

class PuntoOut(PuntoBase):
    id: int

    class Config:
        from_attributes = True

class RutaBase(BaseModel):
    nombre: str
    descripcion: str = ""

class RutaOut(RutaBase):
    id: int
    puntos: List[PuntoOut] = []

    class Config:
        from_attributes = True
