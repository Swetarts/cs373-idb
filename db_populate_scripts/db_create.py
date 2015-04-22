# ---------------------------
# cs373-idb/db_create.py
# Copyright (C) 2015
# Swetarts
# ---------------------------

from server import db

#Here's what you do:
# * Drag the contents of db_populate_scripts out into the root directory.
# * Just run python db_create.py and you're done. It'll take a while to 
#   build the search indices ~30 minutes
print('dropping all tables...', end='')
db.drop_all()
print('done')

print('recreating the schema...', end='')
db.create_all()
print('done')

print('adding publishers...', end='')
import db_populate_publishers
print('done')

print('adding teams...', end='')
import db_populate_teams
print('done')

print('adding powers...', end='')
import db_populate_powers
print('done')

print('adding people...', end='')
import db_populate_people
print('done')

print('adding characters...', end='')
import db_populate_characters
print('done')

print('adding friends_foes...', end='')
import db_populate_friends_foes
print('done')

print('adding comic_issue_and_vol...', end='')
import db_populate_comic_issue_and_vol
print('done')


