// JS Funktionen um die die Bilder der Galerie als Lightboxen darzustellen

let lightbox = document.querySelector("#lightbox_outer"),
    body_gallery = document.querySelector("#body_gallery"),
    loading = document.querySelector("#loading");


lightbox.addEventListener('click', closeLightbox);

let img = document.createElement("img"),
    src = document.getElementById("lightbox"),
    open = false;

function openLightbox(path){
    console.log("open");
    img.src = path;
    src.appendChild(img);
    lightbox.classList.remove("hidden");
    open=true;
}

function closeLightbox(){
    if(open)
    {console.log("close");
    src.removeChild(img);
    lightbox.classList.add("hidden");
    open=false;
    }
}


window.onload = function()
  { setTimeout(function()
    { body_gallery.classList.remove("hidden");
      loading.classList.add("hidden");
    }, 200);
  }