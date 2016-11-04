# coding: utf-8
import requests
import json
from bs4 import BeautifulSoup


# return html of page url
def get_url_contents(url):
    url_handle = requests.get(url)
    return url_handle.content


# gets the json of a single card off the hearthhead website
def get_card_json(contents):
    chowder = BeautifulSoup(contents, "html.parser")

    div = chowder.find(id="main-content")
    text = div.findNext("script").text

    card_json = text[text.index("{\"_id\":"):text.rindex("}")]

    return json.loads(card_json)

# save as .json
def write_to_file(cards, filename):
    with open(filename, "w") as out:
        json.dump(cards, out, indent=4)


# gets url contents and starts card retrieval
def parse_cards(url):
    contents = get_url_contents(url)
    return get_card_json(contents)


def main():
    urlbase = "http://www.hearthhead.com/cards/mana-tide-totem"
    # Card
    cards = parse_cards(urlbase)
    print cards
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
