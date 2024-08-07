# Common shortcuts
run-app:
	docker compose -f docker-compose.yml up

run-test:
	docker compose -f docker-compose.yml exec api pytest .

stop-app:
	docker compose -f docker-compose.yml stop

remove-app:
	docker compose -f docker-compose.yml down

destroy-app:
	docker compose -f docker-compose.yml down -v

# Django commands
create-migrations:
	docker compose -f docker-compose.yml exec api python manage.py makemigrations

migrate:
	docker compose -f docker-compose.yml exec api python manage.py migrate

shell:
	docker compose -f docker-compose.yml exec api python manage.py shell

bash:
	docker compose -f docker-compose.yml exec api bash

test:
	docker compose -f docker-compose.yml exec api pytest .
