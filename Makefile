.PHONY: all clean init

init: clean
	pipenv --python 3.7
	pipenv install

service_up:
	docker-compose up -d

service_down:
	docker-compose down && docker volume rm postgres_data

migrate:
	cd migrations && pipenv run alembic upgrade schema@heads
