# pip or pip3, which ever points to Python 3
pip install pipenv
sleep 10
# activate virtual env
pipenv shell
sleep 10
# install dependencies
pipenv install sqlalchemy psycopg2
# starting a dockerized instance of PostgreSQL
docker run --name sqlalchemy-orm-psql \
    -e POSTGRES_PASSWORD=test \
    -e POSTGRES_USER=test \
    -e POSTGRES_DB=sqlalchemy \
    -p 5432:5432 \
    -d postgres
sleep 10
# stop instance
#docker stop sqlalchemy-orm-psql

# destroy instance
#docker rm sqlalchemy-orm-psql

python -m ./src/initialize/inserts.py
sleep 10
python -m src.services.queries.py
