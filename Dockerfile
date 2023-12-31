FROM python:3.9.18-slim

WORKDIR /app

COPY ./requirements.txt /app/

RUN  apt-get update -y

RUN pip install -r requirements.txt

EXPOSE 5000
COPY . /app/

CMD ["python3", "-m", "api.v1.app"]
