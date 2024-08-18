FROM python:3.11

COPY ./nginx.conf /etc/nginx/conf.d/default.conf
COPY . .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir pipenv
RUN pipenv install --deploy --system

WORKDIR /small_shop
COPY ./entrypoint.sh .
COPY ./env .
RUN cat .env

RUN chmod +x entrypoint.sh

CMD ["./entrypoint.sh"]
