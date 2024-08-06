FROM python:3.12.3

WORKDIR /app

RUN pip install --no-cache-dir pipenv
COPY . .

RUN pipenv install --deploy --system

RUN sed -i 's/\r$//g' /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# ENTRYPOINT ["/app/entrypoint.sh"]
