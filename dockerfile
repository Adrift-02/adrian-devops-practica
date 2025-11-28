FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de tu código
COPY . .

CMD ["python", "tu_script.py"]