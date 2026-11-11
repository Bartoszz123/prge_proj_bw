FROM python:3.11-slim
LABEL authors='Bartosz'

RUN apt-get update && apt-get install -y build-essential && re -rf /var/lib/apt/lists/*

WORKDIR /app
#jeszcze cos tutaj na koncu COPY dodac
COPY ./docker/fastapi/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY config/fastapi /app

# uvicorn app.main:app --host 0.0.0.0 --port 10000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "10000"]
