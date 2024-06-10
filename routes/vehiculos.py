from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List
from config.config import localSession
from models.models import Vehiculo
from schemas.schemas import *

vehiculo = APIRouter()

def get_db():
    db = localSession()
    try:
        yield db
    finally:
        db.close()

@vehiculo.get("/vehiculos", response_model=List[VehiculoSalida], status_code=status.HTTP_200_OK)
def get_all_vehiculos(db: Session = Depends(get_db)):
        vehiculos = db.query(Vehiculo).all()
        if len(vehiculos) == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No hay vehiculos")
        return vehiculos

@vehiculo.get("/vehiculos/{id}", response_model=VehiculoSalida, status_code=status.HTTP_200_OK)
def get_vehiculo(id: int, db: Session = Depends(get_db)):
    vehiculo = db.query(Vehiculo).filter(Vehiculo.id == id).first()
    if vehiculo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vehiculo no encontrado")
    return vehiculo

@vehiculo.post("/vehiculos", response_model=VehiculoSalida, status_code=status.HTTP_201_CREATED)
def add_vehiculo(vehiculo: VehiculoEntrada, db: Session = Depends(get_db)):
    vehic = Vehiculo(**vehiculo.dict())
    db.add(vehic)
    db.commit()
    db.refresh(vehic)
    return vehic

@vehiculo.put("/vehiculos/{id}", response_model=VehiculoSalida, status_code=status.HTTP_201_CREATED)
def update_vehiculo(id: int, vehiculo: VehiculoEntrada, db: Session = Depends(get_db)):
    vehic = db.query(Vehiculo).filter(Vehiculo.id == id).first()
    if vehic is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vehiculo no encontrado")
    vehic = Vehiculo(**vehiculo.dict())
    db.add(vehic)
    db.commit()
    db.refresh(vehic)
    return vehic

@vehiculo.delete("/vehiculos/{id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_vehiculo(id: int, db: Session = Depends(get_db)):
    vehic = db.query(Vehiculo).filter(Vehiculo.id == id).first()
    if vehic is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vehiculo no encontrado")
    db.delete(vehic)
    db.commit()