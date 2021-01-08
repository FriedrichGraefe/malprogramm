let nav_menu = document.querySelector(".nav_menu")
let nav_menu_button = document.querySelector(".nav_menu_button")
let nav_link = document.querySelectorAll(".nav_link")

nav_menu_button.addEventListener("click", toggleMenu)

function toggleMenu(){
    nav_menu.classList.toggle("show_nav_menu")
    nav_menu_button.classList.toggle("close")
    console.log("toggleMenu")
}

nav_link.forEach(
    function(nav_link) {
        nav_link.addEventListener("click", toggleMenu)
    }
)
