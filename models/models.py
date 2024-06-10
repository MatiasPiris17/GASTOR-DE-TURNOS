from config.config import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

class Cliente(Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    apellido = Column(String(50), index=True)
    email = Column(String(50), nullable=False)
    telefono = Column(String(50), nullable=False)

    # turnos= relationship('Turno', back_populates='cliente')

class Vehiculo(Base):
    __tablename__ = 'vehiculos'
    id = Column(Integer, primary_key=True, index=True)
    marca = Column(String(50), index=True)
    modelo = Column(String(50), index=True)
    año = Column(Integer)
    precio = Column(Integer)

    # turnos = relationship('Turno', back_populates='vehiculo')

class Turno(Base):
    __tablename__ = 'turnos'
    id = Column(Integer, primary_key=True)
    fecha = Column(DateTime, default=datetime.utcnow)
    cliente_id = Column(Integer, ForeignKey('clientes.id'))
    vehiculo_id = Column(Integer, ForeignKey('vehiculos.id'))
    tipo = Column(String(50), index=True)

    # cliente = relationship('Cliente', back_populates='turnos')
    # vehiculo = relationship('vehiculo', back_populates='turnos')