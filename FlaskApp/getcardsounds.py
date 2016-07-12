import requests
import json
import string
from bs4 import BeautifulSoup
import os


# helper to get name of soundfile from link provided
def get_sound_name(url):
    count = url.find("sounds")
    return url[count:]


# helper to scrub name of punctuation
def scrub(name):
    remove_map = dict((ord(char), None) for char in string.punctuation)
    return name.translate(remove_map)


# goes to webpage based on card_num, downloads cards' sounds, puts them in card_name/sounds folder
def extract_soundfiles(card_num, card_name):
    url = "http://www.hearthhead.com/card=" + card_num

    # go to webpage based on card_num
    url_handle = requests.get(url)
    content = url_handle.content

    bs = BeautifulSoup(content, "html.parser")
    div = bs.find(id="sounds")

    # pull all mp3 tags
    audio_file = bs.find_all(type='audio/mpeg')

    # download all the mp3s
    for link in audio_file:
        download = "http:" + link.get("src")
        dl_response = requests.get(download)

        # write content of mp3 file to the cardsounds path
        save_file = "static\\sounds\\cardsounds\\" + card_name + "/" + get_sound_name(download)
        save_norm = os.path.normpath(save_file)
        with open(save_norm, "wb") as code:
            code.write(dl_response.content)


# goes through cards in json file and downloads their sounds if they don't already exist
def get_sounds(cards_file):
    cards_json = json.loads(cards_file.read())

    # need card number for hearthhead link, need card name to have something to reference to
    # puts sound files in directory named after card
    for card in cards_json:
        # clean card_name of punctuation so file name isn't messed up
        card_name = scrub(card["name"])

        card_num = str(card["id"])
        print card_name, ": ", card_num

        # create directories to card_name\sounds to put the sound files in
        cardsounds_norm = os.path.normpath("static\\sounds\\cardsounds\\" + card_name + "\\sounds")
        if not os.path.exists(cardsounds_norm):
            os.makedirs(cardsounds_norm)
            extract_soundfiles(card_num, card_name)
            # don't download or create dir if already there


def main():
    file_dir = "minioncards.json"
    cards_file = open(file_dir)

    cardsounds_norm = os.path.normpath("static\\sounds\\cardsounds\\")
    if not os.path.exists(cardsounds_norm):
        os.mkdir(cardsounds_norm)

    get_sounds(cards_file)

    cards_file.close()


if __name__ == "__main__":
    main()
