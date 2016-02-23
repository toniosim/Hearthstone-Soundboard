// get all the elements in class "sound"
var acc = document.getElementsByClassName("sound");
var i;

// assign this function to all of them, plays previous element (an mp3 soundfile)
for (i = 0; i < acc.length; i++) {
    acc[i].onclick = function(){
        this.previousElementSibling.play();
    }
}