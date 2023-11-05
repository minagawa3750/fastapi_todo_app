FROM python:3.11

WORKDIR /app

ENV PYTHONPATH=/app

ENV PYTHONDONTWRITEBYTECODE=1

COPY ./docker/python/requirements.txt .
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./backend/ .

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]