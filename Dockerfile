FROM python:3.10 AS builder

EXPOSE 8000
WORKDIR /app

RUN apt update && apt -y upgrade
RUN apt install -y --no-install-recommends build-essential gcc
COPY requirements.txt /app
RUN python -m pip install --no-cache-dir --upgrade pip
RUN python -m pip install -r requirements.txt --no-cache-dir

COPY . /app

ENTRYPOINT ["python"]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]
