# GESTOR-DE-TURNOS

## Instrucciones de uso
Configuraciones iniciales, ejecute los siguientes comandos en orden:
- python -m venv env
- env\Scripts\activate.bat
- python -m pip install -r requirements.txt


## Levantar bases de datos
- Crear una bases de datos en MySQL en el puerto 3306 con el nombre "gestor_turnos"


## Levantar el servidor 
- uvicorn main:app 
- uvicorn main:app --reload  ("--reload" modo development)


### Documentación
Para las especificaciones de los endpoints ingresar a:
- http://127.0.0.1:8000/docs
