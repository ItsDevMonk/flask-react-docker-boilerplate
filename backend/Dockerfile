FROM python:3.9-slim
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR  /app/backend
RUN pip install --upgrade pip
COPY . /app/backend
RUN pip install -r requirements.txt