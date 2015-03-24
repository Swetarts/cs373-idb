# Environment
To get your application up and running you need a couple of things:
* [npm](https://www.npmjs.com/)
* [Bower](http://bower.io)
* Python 3.4

After you get bower installed, run this command inside of the **root** project directory (cs373-idb)
```bash
$ bower install
```

This will create the directory `www/bower_components` and install all of our front end assets such as Angular and Bootstrap there.

After that create a python virtual environment with
```bash
$ pyvenv-3.4 venv
```

This will create a directory called venv. 

To activate your virtual envrionment run:
```bash
$ source venv/bin/activate
```

Note: You may receive an error while attempting to create the virtual environment in Ubuntu 14.04. Apparently Ubuntu 14.04 was shipped with a broken pyvenv. Do the following. This will create the venv without pip. Get pip in the environment afterwards.

```bash
$ pyvenv-3.4 --without-pip venv
```

Now you can install all of the packages for our flask app and everything *should* work. To do this run
```bash
pip3 install -r requirements.txt
```

# Playing with the database
When you're in the server, to get to the postgreSQL instance
```bash
postgres@swerver:/$ sudo -iu postgres
postgres@swerver:/$ psql
psql (9.3.6)
Type "help" for help.

You are now connected to database "swetards" as user "postgres".
```

## Popular Commands in `psql`
`\connect <dbname>` - connect to that database
`\q` - quit
`\dt` - list tables in database
`\l` - list databases

## IF YOU'RE UPDATING THE SCHEMA
Here's the workflow that we can script later
```bash
swetards=# drop schema public cascade;
NOTICE:  drop cascades to 14 other objects
DETAIL:  drop cascades to table "COMIC_SERIES"
drop cascades to table "CHARACTER"
drop cascades to table "PEOPLE"
drop cascades to table "PUBLISHER"
drop cascades to table "GENDER"
drop cascades to table " COMIC_PEOPLE"
drop cascades to table "CHARACTER_CREATOR"
drop cascades to table "CHARACTER_ENEMY"
drop cascades to table "CHARACTER_ALLY"
drop cascades to table "COMIC_CHARACTERS"
drop cascades to table "POWER"
drop cascades to table "CHARACTER_POWER"
drop cascades to table "TEAM"
drop cascades to table "CHARACTER_TEAM"
DROP SCHEMA
swetards=# create schema public;
CREATE SCHEMA
swetards=# \q

postgres@swerver:/home/swetard/cs373-idb$ psql swetards -f Sweetarts_datamodel.sql
CREATE TABLE
CREATE TABLE
CREATE TABLE
CREATE TABLE
CREATE TABLE
CREATE TABLE
CREATE TABLE
CREATE TABLE
CREATE TABLE
CREATE TABLE
CREATE TABLE
CREATE TABLE
CREATE TABLE
CREATE TABLE
ALTER TABLE
ALTER TABLE
ALTER TABLE
ALTER TABLE
ALTER TABLE
ALTER TABLE
ALTER TABLE
ALTER TABLE
ALTER TABLE
ALTER TABLE
ALTER TABLE
ALTER TABLE
ALTER TABLE

```

# Running the application
* `$ python server.py`
* visit localhost:5000/index.html

# Server Information
The Server lives at `104.239.165.88`

To log in run
```bash
ssh -i .ssh/id_rsa.pub swetard@104.239.165.88
```
Yes, the username is `swetard`. Please get your ssh keys to me **ASAP** so that I can add them to the `authorized_keys` file. K thks
