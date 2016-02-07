var acc = document.getElementsByClassName("sound");
var i;

for (i = 0; i < acc.length; i++) {
    acc[i].onclick = function(){
        this.previousElementSibling.play();
    }
}