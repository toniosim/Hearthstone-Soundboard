#this script creates the necessary directories and db tables for the card and sounds info
#and fills in the db tables

import sqlite3
import json
import os
import string

#getting the punctuation out so we can name files correctly
def scrub(name):
	remove_map = dict((ord(char), None) for char in string.punctuation)
	return name.translate(remove_map)

cards_file = open("minioncards.json")
cards_json = json.loads(cards_file.read() )

#get cardsounds path based off dir that we're in
#MUST EDIT THIS DOESN'T WORK WITH LINUX (or mac??) FFS
rel_dir = os.path.realpath(".") + "/static/sounds/cardsounds"
sound_dir = os.path.normpath(rel_dir)

cards_conn = sqlite3.connect("cards.db")
sounds_conn = sqlite3.connect("cardsounds.db")

print "Connect Success!"

cards_conn.execute("DROP TABLE IF EXISTS cards")
sounds_conn.execute("DROP TABLE IF EXISTS sounds")

cards_conn.execute("""CREATE TABLE cards(
	cardid INT PRIMARY KEY NOT NULL,
	cardname TEXT NOT NULL,
	cardset TEXT NOT NULL,
	cardclass TEXT);
	""")

print "Cards Table Created Successfully"

sounds_conn.execute("""CREATE TABLE sounds (
	cardid INT NOT NULL,
	cardname TEXT NOT NULL,
	soundfile TEXT NOT NULL);
	""")

print "Sounds Table Created Successfully"

for card in cards_json:
	#enter data from JSON files
	card_values = [card["id"], card["name"],card["set"], card["class"] ]
	cards_conn.execute("""INSERT INTO cards (cardid, cardname, cardset, cardclass) 
		VALUES (?, ?, ?, ?)""", card_values)

	#build the path to [cardname] soundfiles, then list soundfiles
	cardname_clean = scrub(card["name"])
	sound_path = os.path.normpath(sound_dir  + "/" + cardname_clean + "/sounds/")
	sound_files = [f for f in os.listdir(sound_path)]

	#enter sound files into db
	for x in range(len(sound_files) ):
		sound_values = [card["id"], cardname_clean, sound_files[x] ]
		sounds_conn.execute("""INSERT INTO sounds( cardid, cardname, soundfile)
			VALUES (?, ?, ?)""", sound_values )


cards_conn.commit()
sounds_conn.commit()

cards_conn.close()
sounds_conn.close()

