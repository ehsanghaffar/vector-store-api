FROM python:3.11.7

WORKDIR /app

RUN pip install --upgrade pip

COPY ./requirements.txt ./

RUN pip install -r /app/requirements.txt

COPY . .

