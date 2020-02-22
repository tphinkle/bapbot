#

# Flask
1. Export FLASK_APP: `export FLASK_APP=bapbot`
2. Start the flask server `flask run`

# PostgreSQL
## Setting up the postgres server
1. Log into root: `sudo su -`
2. Install postgresql `apt-get install postgresql postgresql-contrib`
3. Configure postgresql to start upon server boot `update-rc.d posstgresql enable`
4. Start the server `service postgresql start`

## Connecting to PostgreSQL
1. Log into postgres user: `su - postgres`
2. Log into database `psql`
3. To exit, type `\q`

## Setting up connection via Python
1. Install packages in `requirements.txt`
2. Follow instructions here https://stackoverflow.com/questions/28253681/you-need-to-install-postgresql-server-dev-x-y-for-building-a-server-side-extensi

## Commands
- `CREATE DATABASE bapdb;`
- Get list of all databases `\l`
- Connect to database `\connect DBNAME`
