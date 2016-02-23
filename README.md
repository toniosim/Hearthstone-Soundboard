A soundboard based off Blizzard's popular game Hearthstone!

This project uses user Ducino's python scripts that pulled JSON info about Hearthstone cards
from Hearthhead.com. I then forked the project (under name hearthstone) to also filter out the minions
and scrape the card sounds from the website (Not all are currently there).

This web app was built using Python 2.7, BeautifulSoup4, Flask, and Sqlite3.

-----v0.1------

Basic funcionality finished! As in, here's all the sounds that could be scraped from Hearthead on an html page!

Future Functionality:
- Filtering based off class/set.
- Actually have it hosted somewhere online

------------------------------


If you just can't wait for me to host it/wanna mess with it yourself:

Required:
Python 2.7
SQLlite3
Flask

- Clone it to your computer
- run the python scripts in this order:
	-- getcard.py (will give you hero/hero power .jsons as well)
	-- getminion.py
	-- getcardsounds.py (may takea while)
	-- connect.py
- run the app.py script
- while it's running, point your browser to localhost:5000
* all the sound files currently download once you enter the index page, will be fixed