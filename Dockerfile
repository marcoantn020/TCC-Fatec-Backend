FROM python:3.7-slim

WORKDIR /var/www/app/

COPY requirements.txt requirements.txt

RUN python -m pip install --upgrade pip

RUN pip3 install -r requirements.txt

COPY . /var/www/app/

EXPOSE 80