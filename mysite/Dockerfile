FROM python:3.11
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . /usr/src/app

CMD gunicorn mysite.wsgi:application --bind 0.0.0.0:$PORT
