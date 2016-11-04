A soundboard based off Blizzard's popular game Hearthstone!

This project uses user Ducino's python scripts (https://github.com/ducino/hearthstone) that pulled JSON info about Hearthstone cards from Hearthhead.com. I added functionality to filter
out the minions and scrape the card sounds from the old version of HearthHead (Not all are currently there).

This web app was built using Python 2.7, BeautifulSoup4, Flask, and Sqlite3. You can use the requirements.txt file to install the necessary dependencies using pip install -r requirements.txt. I recommend setting up a virtual environment.


The plan is to eventually get this hosted on a site for people to enjoy but the functionality isn't quite there yet. The current getcards.py is broken since HearthHead changed the layout of the site, but the card.json file should have everything up to (and including) Whispers of the Old Gods. 

When all the scripts are running they run in this order:
	-- getcard.py (will give you hero/hero power .jsons as well) (does not currently work)
	-- getminion.py
	-- getcardsounds.py
	-- connect.py
	-- app.py to get it started
- while it's running, point your browser to localhost:5000