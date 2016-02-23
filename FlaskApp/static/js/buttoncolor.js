// getting passed the card class, which determines color of the button, assigned via card_id
function assignColor(card_id, card_class) {
	//warrior:
	if(card_class == 1) {
		color = "#7b0323";

	//paladin:
	}else if(card_class == 2) {
		color = "#fdee73";

	//hunter:
	}else if(card_class == 3) {
		color = "#63b365";

	//rogue
	}else if(card_class == 4) {
		color = "#343837";

	//priest
	}else if(card_class == 5) {
		color = "#b7c9e2";

	//shaman
	}else if(card_class == 7) {
		color = "#26538d";

	//mage:
	}else if(card_class == 8) {
		color = "#c3fbf4";

	//warlock:
	}else if(card_class == 9) {
		color = "#916e99";

	//druid:
	}else if(card_class == 11) {
		color = "#a9561e";

	//neutral:
	}else {
		color = "#ddd";
	}

	document.getElementById(card_id).style.background = color;
}