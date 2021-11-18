createenv:
	python3 -m venv gamelib-env
setenv:
	source ../gamelib-env/bin/activate
createproject:
	django-admin startproject djangoproject
createapp:
	./manage.py startapp gamelib
installenv:
	pip3 install django-environ
installpsycopg2:
	pip3 install psycopg2-binary
remotedb:
	docker exec -it gamelibenv-env_db_1 /bin/bash
	docker exec -it djangoproject_db_1 /bin/bash
psql:
	psql -d devduo -U root -W
dbup:
	docker-compose -f docker-compose.yml --env-file ./myapp/.env up -d
	docker-compose -f docker-compose.yml --env-file ./djangoproject/.env up -d
dbdown:
	docker-compose -f docker-compose.yml down --volumes