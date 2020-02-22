# 

# PostgreSQL
## Setting up the postgres server
1. Log into root: `sudo su -`
2. Install postgresql `apt-get install postgresql postgresql-contrib`
3. Configure postgresql to start upon server boot `update-rc.d posstgresql enable`
4. Start the server `servie postgresql start`

## Connecting to PostgreSQL
1. Log into postgres user: `su - postgres`
2. Log into database `psql`
3. To exit, type `\q`

## Commands
- `CREATE DATABASE bapdb;`
- Get list ofo all databases `\l`

