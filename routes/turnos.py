from config.config import localSession
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List
from config.config import localSession
from models.models import Turno
from schemas.schemas import *

turno = APIRouter()

def get_db():
    db = localSession()
    try:
        yield db
    finally:
        db.close()


@turno.get("/turnos", response_model=List[TurnoSalida], status_code=status.HTTP_200_OK)
def get_all_turnos(db: Session = Depends(get_db)):
    turnos = db.query(Turno).all()
    if len(turnos) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No hay turnos")
    return turnos


@turno.get("/turnos/{id}", response_model=List[TurnoSalida], status_code=status.HTTP_200_OK)
def get_turno(id: int, db: Session = Depends(get_db)):
    cliente = db.query(Turno).filter(Turno.id == id).first()
    if cliente is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Turno no encontrado")
    return cliente


@turno.post("/turnos", response_model=TurnoEntrada, status_code=status.HTTP_201_CREATED)
def add_turno(turno: TurnoEntrada, db: Session = Depends(get_db)):
    turn = Turno(**turno.dict())
    db.add(turn)
    db.commit()
    db.refresh(turn)
    return turn


@turno.put("/turnos/{id}", response_model=TurnoSalida, status_code=status.HTTP_201_CREATED)
def update_turno(id: int, turno: TurnoEntrada, db: Session = Depends(get_db)):
    turn = db.query(Turno).filter(Turno.id == id).first()
    if turn is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Turno no encontrado")
    turn = Turno(**turno.dict())
    db.add(turn)
    db.commit()
    db.refresh(turn)
    return turn


@turno.delete("/turnos/{id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_turno(id: int, db: Session = Depends(get_db)):
    turn = db.query(Turno).filter(Turno.id == id).first()
    if turn is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Turno no encontrado")
    db.delete(turn)
    db.commit()


# Buscar todos los turnos de un cliente
@turno.get("/turnos/cliente/{id}", response_model=List[TurnoSalida], status_code=status.HTTP_200_OK)
def get_turnos_cliente(id: int, db: Session = Depends(get_db)):
    turnos_cliente = db.query(Turno).filter(Turno.cliente_id == id).all()
    if len(turnos_cliente) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No hay turnos para el cliente")
    return turnos_cliente


# Buscar todos los turnos de un vehiculo
@turno.get("/turnos/vehiculo/{id}", response_model=List[TurnoSalida], status_code=status.HTTP_200_OK)
def get_turnos_vehiculo(id: int, db: Session = Depends(get_db)):
    turnos_vehiculo = db.query(Turno).filter(Turno.vehiculo_id == id).all()
    if len(turnos_vehiculo) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No hay turnos para el vehiculo")
    return turnos_vehiculo