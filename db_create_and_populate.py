#!/usr/local/bin python3
from server import db

db.drop_all()
import db_create

print(" Loading: db_populate_publishers.py")
import db_populate_publishers

print(" Loading: db_populate_teams.py")
import db_populate_teams

print(" Loading: db_populate_powers.py")
import db_populate_powers

print(" Loading: db_populate_people.py")
import db_populate_people

print(" Loading: db_populate_characters.py")
import db_populate_characters

print(" Loading: db_populate_friends_foes")
import db_populate_friends_foes

print(" Loading: db_populate_comics.py")
import db_populate_comic_issue_and_vol

print('Done!')