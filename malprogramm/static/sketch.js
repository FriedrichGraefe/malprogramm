//Steuerung:
//A: Opacity ändern
//S: Umrisslinie an/aus
//D: Hintergrundfarbe ändern
//F: KreisFarbe ändern
//C: Kreise löschen
//T: Lokal speichern

var linie = 3;
var liniebool = true;
var opacity = 255;
var o = 0;
var r = 252;
var g = 195;
var f = 0;
var b = 0;
var bg0 = 32;
var bg1 = 222;
var bg2 = 200;



function setup() {
    let cnv =createCanvas(windowWidth, windowHeight);
    cnv.id('mycanvas');
    cnv.background(bg0, bg1, bg2);
}

function draw() {

//zum Zeichnen muss man die Maus gedrückt halten
    if (mouseIsPressed === true) {
        variableEllipse(mouseX, mouseY, pmouseX, pmouseY);
    }

    if(liniebool === true){
        linie = 3;
    }else{
        linie = 0;
    }


}

function variableEllipse(x, y, px, py) {
    let speed = abs(x - px) + abs(y - py);
    stroke(bg0, bg1, bg2);
    strokeWeight(linie);
    fill(r, g, speed, opacity);
    ellipse(x, y, speed, speed);
}

//Kreise löschen
function keyPressed() {
    if (keyCode === 67) {
        clear();
        background(bg0, bg1, bg2);
    }

//Umrisslinie
    if (keyCode === 83) {
        liniebool = !liniebool;
    }

//Opacity
    if (keyCode === 65) {

        if (o === 0){
            opacity = 150;
            o = o + 1;
        } else if (o === 1){
            opacity = 50;
            o = o + 1;
        } else {
            opacity = 255;
            o = 0;
        }
    }

//Kreisfarbe
    if (keyCode === 70) {

        if (f === 0){
            r = 250;
            g = 75;
            f = f + 1;
        } else if (f === 1){
            r = 100;
            g = 200;
            f = f + 1;
        } else {
            r = 252;
            g = 195;
            f = 0;
        }
    }

//Hintergrundfarbe
    if (keyCode === 68) {

        if (b === 0){
            bg0 = 250;
            bg1 = 100;
            bg2 = 100;
            background(bg0, bg1, bg2);
            b = b + 1;
        } else if (b === 1){
            bg0 = 32;
            bg1 = 100;
            bg2 = 200;
            background(bg0, bg1, bg2);
            b = b + 1;
        } else {
            bg0 = 32;
            bg1 = 222;
            bg2 = 200;
            background(bg0, bg1, bg2);
            b = 0;
        }
    }

    if (keyCode === 84) {
        saveCanvas('myCanvas', 'jpg');
    }


}
