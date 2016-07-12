#create a json file of just minions, chang empty class to neutral
import json

# only want the minions
def parse_minions(filename):
	minions_list = []
	cards_json = json.loads(open(filename).read() )

	for card in cards_json:
		if card["type"] == 4: # 4 = minion
			minions_list.append(card)
			

	return minions_list

def write_to_file(cards, filename):
	with open(filename, "w") as out:
		json.dump(cards, out, indent=4)

# give the card a class if it's neutral
def normalize_cards(cards_json):
	for card in cards_json:
		if 'class' not in card:
			card["class"] = 0


	return cards_json

def main():
	outfile = "minioncards.json"
	infile = "card.json"

	print "Extracting Minions..."
	cards = parse_minions(infile)
	normalize_cards(cards)
	write_to_file(cards, outfile)
	print "...Done!"


if __name__ == "__main__":
	main()
