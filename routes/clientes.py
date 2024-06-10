from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List
from config.config import localSession
from models.models import Cliente
from schemas.schemas import *

cliente = APIRouter()

def get_db():
    db = localSession()
    try:
        yield db
    finally:
        db.close()

@cliente.get("/clientes", response_model=List[ClienteSalida], status_code=status.HTTP_200_OK)
def get_all_clientes(db: Session = Depends(get_db)):
    clientes = db.query(Cliente).all()
    if len(clientes) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No hay contactos")
    return clientes

@cliente.get("/clientes/{id}", response_model=ClienteSalida, status_code=status.HTTP_200_OK)
def get_cliente(id: int, db: Session = Depends(get_db)):
    cliente = db.query(Cliente).filter(Cliente.id == id).first()
    if cliente is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contacto no encontrado")
    return cliente

@cliente.post("/clientes", response_model=ClienteSalida, status_code=status.HTTP_201_CREATED)
def add_contacto(contacto: ClienteEntrada, db: Session = Depends(get_db)):
    contact = Cliente(**contacto.dict())
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact

@cliente.put("/clientes/{id}", response_model=ClienteSalida, status_code=status.HTTP_201_CREATED)
def update_contacto(id: int, contacto: ClienteEntrada, db: Session = Depends(get_db)):
    contact = db.query(Cliente).filter(Cliente.id == id).first()
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contacto no encontrado")
    contact = Cliente(**contacto.dict())
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact

@cliente.delete("/clientes/{id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_contacto(id: int, db: Session = Depends(get_db)):
    contact = db.query(Cliente).filter(Cliente.id == id).first()
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contacto no encontrado")
    db.delete(contact)
    db.commit()