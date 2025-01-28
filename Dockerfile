# Usar una imagen base de Python oficial
FROM python:3.12-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo requirements.txt al directorio de trabajo
COPY requirements.txt .

# Instalar las dependencias necesarias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de la aplicación al directorio de trabajo
COPY main.py .

# Exponer el puerto en el que la aplicación escuchará
EXPOSE 8000

# Definir la variable de entorno para evitar buffers de salida
ENV PYTHONUNBUFFERED=1

# Comando para ejecutar la aplicación
CMD ["python", "main.py"]