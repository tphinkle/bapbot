#

# EC2
1. Set up security group to allow inbound and outbound traffic, see: https://aws.amazon.com/premiumsupport/knowledge-center/connect-http-https-ec2/
and
https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html#WorkingWithSecurityGroups
2. Attach the security group to EC2 instance

# Configuring the server
1. See https://www.datasciencebytes.com/bytes/2015/02/24/running-a-flask-app-on-aws-ec2/
  - Check error logs: `/var/log/apache2/error.log`
  - Configure to take custom python path:

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
