let lightbox = document.querySelector("#lightbox_outer");


lightbox.addEventListener('click', closeLightbox);

let img = document.createElement("img");
let src = document.getElementById("lightbox");

function openLightbox(path){
    console.log("open");
    img.src = path;
    src.appendChild(img);
    lightbox.classList.remove("hidden");
}

function closeLightbox(){
    console.log("close");
    src.removeChild(img);
    lightbox.classList.add("hidden");
}