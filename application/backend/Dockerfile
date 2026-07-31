FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN useradd -m bankuser && \
    chown -R bankuser:bankuser /app

USER bankuser

EXPOSE 8080

CMD ["python", "app.py"]
