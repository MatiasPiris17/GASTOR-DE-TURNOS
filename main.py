from fastapi import FastAPI
from config.config import engine
from models import models
from routes.clientes import cliente
from routes.vehiculos import vehiculo
from routes.turnos import turno

models.Base.metadata.create_all(bind=engine)

app = FastAPI();
app.include_router(turno)
app.include_router(cliente)
app.include_router(vehiculo)
