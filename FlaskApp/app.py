from flask import Flask, render_template, request, redirect, g
import sqlite3
import os, sys

app = Flask(__name__)
app_title = "Hearthstone Soundboard"
author = "Tonio Simonetta"
rel_dir = os.path.realpath(".") + "/static/sounds/cardsounds"
sound_dir = os.path.normpath(rel_dir)

@app.route("/")
def main():
	card_conn = sqlite3.connect("cards.db")
	sound_conn = sqlite3.connect("cardsounds.db")

	card_conn.row_factory = sqlite3.Row
	sound_conn.row_factory = sqlite3.Row


	card_cur = card_conn.cursor()
	sound_cur = sound_conn.cursor()

	card_cur.execute("SELECT * FROM cards ORDER BY cardname ASC")
	sound_cur.execute("SELECT * FROM sounds ORDER BY cardname ASC")

	card_rows = card_cur.fetchall()
	sound_rows = sound_cur.fetchall()

	card_conn.close()
	sound_conn.close()

	return render_template("index.html", app_title=app_title, author=author, card_rows=card_rows, sound_rows=sound_rows)


if __name__ == "__main__":
	app.run(debug=True)