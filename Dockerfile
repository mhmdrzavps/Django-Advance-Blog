FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 

WORKDIR /app

COPY requirements.txt  /app/

RUN pip install --upgrade pip --proxy http://host.docker.internal:10809
RUN pip install -r requirements.txt --proxy http://host.docker.internal:10809

COPY ./core /app/

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

