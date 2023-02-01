# DockerBackend_Kitbuilder
Tutorial from Very Academy (YT) - "Build your first API with Python's Fastest API Web Framework!"

Wrote docker-compose.yml then used (in terminal):
    docker-compose up

requirements.txt was made using "pip freeze > requirements.txt

To run migration:
docker-compose run app alembic revision --autogenerate -m "New Migration"
docker-compose run app alembic upgrade head