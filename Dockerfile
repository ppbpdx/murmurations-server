FROM python:3.7

COPY ./requirements.txt /usr/src/app/requirements.txt

WORKDIR /usr/src/app

RUN pip install -r requirements.txt

COPY . /usr/src/app

EXPOSE 5000

CMD ["gunicorn" ,"-b 0.0.0.0:5000", "manage:app"]