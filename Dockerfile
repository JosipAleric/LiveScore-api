# Koristi prikladnu osnovnu sliku za FastAPI aplikaciju
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# Postavi radni direktorij
WORKDIR /app

# Kopiraj requirements.txt i instaliraj ovisnosti
COPY requirements.txt .
RUN pip install -r requirements.txt

# Kopiraj sve ostale datoteke
COPY . .

# Expose port
EXPOSE 8000

# Pokreni aplikaciju
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
