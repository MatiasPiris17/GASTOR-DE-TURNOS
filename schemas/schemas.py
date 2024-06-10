from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class ClienteEntrada(BaseModel):
    nombre: str
    email: str
    telefono: str

class ClienteSalida(BaseModel):
    id: Optional[int] = None
    nombre: str
    email: str
    telefono: str


class TurnoEntrada(BaseModel):
    fecha: datetime
    tipo: str
    cliente_id: int
    vehiculo_id: int

    class Config:
        orm_mode = True

class TurnoSalida(BaseModel):
    id: Optional[int] = None
    fecha: datetime
    tipo: str
    cliente_id: int
    vehiculo_id: int


class VehiculoEntrada(BaseModel):
    marca: str
    modelo: str
    año: int
    precio:int

class VehiculoSalida(BaseModel):
    id: Optional[int] = None
    marca: str
    modelo: str
    año: int
    precio:int

    class Config:
        orm_mode = True