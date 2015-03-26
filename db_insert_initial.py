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
    # Character(
    # id='1698',
    # name='Catwoman',
    # alias='Selina Kyle Selina Falcone Selina Wayne Batwoman Belinda Elva Barr Irena Dubrovna Kitty Grimalkin Madame Moderne Marguerite Tone Roxy Rocket Sadie Kelowski The Cat The Cat Burglar Catbird',
    # image='http://static.comicvine.com/uploads/scale_medium/10/100647/4174482-catwoman+cover+35.jpg',
    # description='Catwoman, the costumed alias persona of Selina Kyle, is a mostly reformed cat burglar with an on-again, off-again, romantic relationship with Batman. She is shown as a woman who is very strong-willed, independent and morally conflicted with her past.',
    # gender='Female',
    # origin='Human'
    # )
    # ally = character
    # enemy = character
    # power = Power(
    # id=4,
    # name='Agility'
    # )
    # power2 = Power(
    # id=35,
    # name='Gadgets'
    # )
    # team = Team(
    # id=22672,
    # name='Injustice League'
    # )
    #
 	# Character(
    # id='1440',
    # name='Wolverine',
    # alias='James Howlett Logan Agent Ten Black Dragon Brother Xavier Captain Canada Captain Terror Death Emilio Garra Experiment X Fist of Legend Hooded Man Jim Logan John Logan Mutate #9601 Patch Peter Richards Revolto the Clown Weapon X',
    # image='http://static.comicvine.com/uploads/scale_medium/3/39027/2750376-548830_10151203899618598_1220495592_n.jpg',
    # description='A long-lived mutant with the rage of a beast and the soul of a Samurai, James \"Logan\" Howlett\'s past is filled with blood, war, and betrayal. Possessing an accelerated healing factor, enhanced senses, and bone claws in his hands that, along with his skeleton, are coated in adamantium, Wolverine is the ultimate weapon.',
    # gender='Male',
    # origin='Mutant'
    # )
    # ally = character
    # enemy = character
    # power = Power(
    # id=2,
    # name='Super Strength')
    # power2 = Power(
    # id=40,
    # name='Immortal')
    # team = Team(
    # id=3173,
    # name='X-Men')
    #
 	# Character(
    # id='1807',
    # name='Superman',
    # alias='Kal-El Clark Kent Clark Jerome Kent Clark Joseph Kent Gangbuster Nightwing Jordan Elliot Superboy Superman-Prime The Action Ace The Big Blue Boy Scout The Last Son of Krypton The Man of Might The Man of Steel The Man of Tomorrow Marc Costa Nembo Kid',
    # image='http://static.comicvine.com/uploads/scale_medium/7/73958/4455245-sup.jpg',
    # description='Rocketed to Earth as an infant from the doomed planet Krypton, Kal-El was adopted by the loving Kent family and raised in America\'s heartland as Clark Kent. Using his immense solar-fueled powers, he became Superman to defend mankind against all manner of threats while championing truth, justice and the American way!',
    # gender='Male',
    # origin='Mutant'
    # )
    # ally = character
    # enemy = character
    # power = Power(
    # id=2,
    # name='Super Strength')
    # power2 = Power(
    # id=1,
    # name='Flight')
    # team = Team(
    # id=31815,
    # name='Justice League of America'
    # )),
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
