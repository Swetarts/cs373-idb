from models import Character, Person, Comic_Series, Publisher, Power, Team
from server import db


character = Character (
	id='1253',
	name='Lightning Lad',
	alias='Garth Ranzz Lightning Boy Proty Live Wire Starfinger Lightning Man',
	image='http://static.comicvine.com/uploads/square_avatar/2/28079/1923024-garth_ranzz__06__002__01_.png',
	description='Garth Ranzz was born on the agricultural world of Winath with his twin, Ayla.',
	gender='Male',
	origin='Alien'
	)
ally = character
enemy = character
power = Power(
	id=1,
	name='Flight')
power2 = Power(
	id=14,
	name='Blast Power')
team = Team(
	id=19241,
	name='Legion of Superheroes')
character.allies.append(ally)
character.enemies.append(enemy)
character.powers.append(power)
character.powers.append(power2)
character.teams.append(team)
db.session.add(character)
db.session.commit()
# characters = [
# 	Character(),
# 	Character(),
# 	Character(),
# 	Character(),
# 	Character(),
# 	Character(),
# 	Character(),
# 	Character(),
# 	Character(),
# 	Character()]

# people = [
# 	Person(),
# 	Person(),
# 	Person(),
# 	Person(),
# 	Person(),
# 	Person(),
# 	Person(),
# 	Person(),
# 	Person(),
# 	Person()]

# series = [
# 	Comic_Series(),
# 	Comic_Series(),
# 	Comic_Series(),
# 	Comic_Series(),
# 	Comic_Series(),
# 	Comic_Series(),
# 	Comic_Series(),
# 	Comic_Series(),
# 	Comic_Series(),
# 	Comic_Series()]

# publshers = [
# 	Publisher(),
# 	Publisher(),
# 	Publisher(),
# 	Publisher(),
# 	Publisher(),
# 	Publisher(),
# 	Publisher(),
# 	Publisher(),
# 	Publisher(),
# 	Publisher()]

# powers = [
# 	Power(),
# 	Power(),
# 	Power(),
# 	Power(),
# 	Power(),
# 	Power(),
# 	Power(),
# 	Power(),
# 	Power(),
# 	Power()]

# teams = [
# 	Team(),
# 	Team(),
# 	Team(),
# 	Team(),
# 	Team(),
# 	Team(),
# 	Team(),
# 	Team(),
# 	Team(),
# 	Team()]

# [db.session.add(x) for x in characters]
# db.session.commit()
