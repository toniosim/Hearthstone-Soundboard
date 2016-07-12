# coding: utf-8
import requests
import json
from bs4 import BeautifulSoup


# return contents based off url
def get_url_contents(url):
    url_handle = requests.get(url)
    return url_handle.content


# gets each card off hearthhead.com/cards in json format
def get_cards_json(contents):
    bs = BeautifulSoup(contents)
    div = bs.find(id="lv-hearthstonecards")
    text = div.findNext("script").text

    start = text.find("var hearthstoneCards")
    cards_json = text[text.find("[", start):text.find("]", start) + 1]

    valid_cards_json = cards_json.replace("popularity:", '"popularity":')
    valid_cards_json = valid_cards_json.replace("classs", "class")
    return json.loads(valid_cards_json)


# save as .json
def write_to_file(cards, filename):
    with open(filename, "w") as out:
        json.dump(cards, out, indent=4)


# gets url contents and starts card retrieval
def parse_cards(url):
    contents = get_url_contents(url)
    return get_cards_json(contents)


def main():
    urlbase = "http://www.hearthhead.com/cards=4.0"
    # Card
    cards = parse_cards(urlbase)
    write_to_file(cards, "card.json")
    print "...Card done!"
    # Hero
    #cards = parse_cards(urlbase + "?filter=type=3")
    #write_to_file(cards, "hero.json")
    #print "...Hero done!"
    # Hero Power
    #cards = parse_cards(urlbase + "?filter=type=10")
    #write_to_file(cards, "hpower.json")
    #print "...HeroPower done!"


if __name__ == "__main__":
    main()
