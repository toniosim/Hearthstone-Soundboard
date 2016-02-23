// get all in class "accordian"
var acc = document.getElementsByClassName("accordion");
var i;

// assign onclick function to toggle "active" and "show" classes,
// which show the panel that's being clicked
for (i = 0; i < acc.length; i++) {
    acc[i].onclick = function(){
        this.classList.toggle("active");
        this.nextElementSibling.classList.toggle("show");
    }
}