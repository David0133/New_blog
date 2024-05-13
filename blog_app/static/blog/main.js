
const dot = document.querySelectorAll(".dot")[0];
let change = document.getElementsByClassName("change-menu");
const back = document.getElementsByClassName("back");

dot.addEventListener("click", () => {
    change[0].style.display = "flex";
    back[0].style.display = "flex";
    dot.style.display = "none";
})

document.getElementsByClassName('blog-content')[0].addEventListener("click", () => {
    change[0].style.display = "none";
    back[0].style.display = "none";
    dot.style.display = "block";
})

back[0].addEventListener("click", () => {
    change[0].style.display = "none";
    back[0].style.display = "none";
    dot.style.display = "block";
})



