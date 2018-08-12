function myFunction(bar) {
    bar.classList.toggle("change");
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
        x.className += " responsive";
    } else {
        x.className = "topnav";
    }
}

// function thisFunction(x) {
//     x.classList.toggle("change");
// }