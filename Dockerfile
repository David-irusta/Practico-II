#Imagen madre
FROM python:3.11-slim

#Configuracion para poder ver los logs de manera correcta
ENV PYTHONUNBUFFERED=1

#Directorio de trabajo (donde vamos a pararnos)
WORKDIR /crud

#Copiar archivos de depencencias
COPY requirements.txt /crud/

#Instalar las dependencias via pip
RUN pip install -r requirements.txt

#Copiamos codigo fuente del proyecto 
COPY crud/ .