FROM python:3.11-slim

# Instalar Tesseract + idiomas español e inglés
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    tesseract-ocr-spa \
    tesseract-ocr-eng \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libgomp1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Directorio de trabajo
WORKDIR /app

# Instalar dependencias Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el proyecto
COPY . .

# Crear carpeta de uploads
RUN mkdir -p uploads

# Puerto que expone Render
ENV PORT=10000
EXPOSE 10000

# Comando de inicio
CMD gunicorn app:app --bind 0.0.0.0:$PORT
