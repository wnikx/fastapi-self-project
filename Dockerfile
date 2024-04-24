FROM python:3.10-alpine

WORKDIR /fastapi_app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "src.main:app", "--reload", "--bind=0.0.0.0:8000"]