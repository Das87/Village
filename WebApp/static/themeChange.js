var x = document.getElementById("left1");
x.addEventListener("mouseover", myFunction1);
x.addEventListener("click", mySecondFunction1);
x.addEventListener("mouseout", myThirdFunction1);

function myFunction1() {
  //Background changing bby hovering
  document.getElementById("back1").style.background = "linear-gradient(rgb(255, 60, 0), black, green)"
  //BARWADIH becomes red during mouseover
  document.getElementById("name").style.color = "red"
  x.style.height = "110px";
  x.style.opacity = "1"


}

function mySecondFunction1() {
  //Background changing bby hovering
  document.getElementById("back1").style.background = "linear-gradient(rgb(255, 60, 0), black, green)"
  //BARWADIH becomes red during mouseover
  document.getElementById("name").style.color = "red"
  x.style.height = "110px";
  x.style.opacity = "1"

}

function myThirdFunction1() {
  document.getElementById("back1").style.background = "linear-gradient(rgb(255, 60, 0), yellow, rgb(16, 201, 16))";
  //again BARWADIH becomes black
  document.getElementById("name").style.color = "black"
  x.style.height = "100px";
  x.style.opacity = "0.1"



}
//--------------------------------------------------------
//left2

var y = document.getElementById("left2");
y.addEventListener("mouseover", myFunction2);
y.addEventListener("click", mySecondFunction2);
y.addEventListener("mouseout", myThirdFunction2);

function myFunction2() {
  //Background changing bby hovering
  document.getElementById("back1").style.background = "linear-gradient(rgb(0, 94, 255), rgb(238, 50, 50), rgb(224, 21, 187))"
  //BARWADIH becomes red during mouseover
  document.getElementById("name").style.color = "white"
  y.style.height = "110px";
  y.style.opacity = "1"
}
function mySecondFunction2() {
  //Background changing bby hovering
  document.getElementById("back1").style.background = "linear-gradient(rgb(0, 94, 255), rgb(238, 50, 50), rgb(224, 21, 187))"
  //BARWADIH becomes red during mouseover
  document.getElementById("name").style.color = "white"
  y.style.height = "110px";
  y.style.opacity = "1"
}

function myThirdFunction2() {
  document.getElementById("back1").style.background = "linear-gradient(rgb(255, 60, 0), yellow, rgb(16, 201, 16))";
  //again BARWADIH becomes black
  document.getElementById("name").style.color = "black"
  y.style.height = "100px";
  y.style.opacity = "0.1"

}

//-----------------------------------------------------
//right2 
var z = document.getElementById("right2");
z.addEventListener("mouseover", myFunction3);
z.addEventListener("click", mySecondFunction3);
z.addEventListener("mouseout", myThirdFunction3);

function myFunction3() {
  //Background changing bby hovering
  document.getElementById("back1").style.background = "linear-gradient(rgb(200, 255, 0), rgb(245, 14, 14), black)"
  //BARWADIH becomes red during mouseover
  document.getElementById("name").style.color = "rgb(170, 194, 236)"
  z.style.height = "110px";
  z.style.opacity = "1";
}
function mySecondFunction3() {
  //Background changing bby hovering
  document.getElementById("back1").style.background = "linear-gradient(rgb(200, 255, 0), rgb(245, 14, 14), black)"
  //BARWADIH becomes red during mouseover
  document.getElementById("name").style.color = "rgb(170, 194, 236)"
  z.style.height = "110px";
  z.style.opacity = "1";
}


function myThirdFunction3() {
  document.getElementById("back1").style.background = "linear-gradient(rgb(255, 60, 0), yellow, rgb(16, 201, 16))";
  //again BARWADIH becomes black
  document.getElementById("name").style.color = "black"
  z.style.height = "100px";
  z.style.opacity = "0.1"

}

//--------------------------------------------------
//right1

var k = document.getElementById("right1");
k.addEventListener("mouseover", myFunction4);
k.addEventListener("click", mySecondFunction4);
k.addEventListener("mouseout", myThirdFunction4);

function myFunction4() {
  //Background changing bby hovering
  document.getElementById("back1").style.background = "linear-gradient(rgb(0, 21, 255), rgb(4, 246, 202), rgb(4, 164, 2))"
  //BARWADIH becomes red during mouseover
  document.getElementById("name").style.color = "red";
  k.style.height = "110px";
  k.style.opacity = "1";
}
function mySecondFunction4() {
  //Background changing bby hovering
  document.getElementById("back1").style.background = "linear-gradient(rgb(0, 21, 255), rgb(4, 246, 202), rgb(4, 164, 2))"
  //BARWADIH becomes red during mouseover
  document.getElementById("name").style.color = "red";
  k.style.height = "110px";
  k.style.opacity = "1";
}
function myThirdFunction4() {
  document.getElementById("back1").style.background = "linear-gradient(rgb(255, 60, 0), yellow, rgb(16, 201, 16))";
  //again BARWADIH becomes black
  document.getElementById("name").style.color = "black"

  k.style.height = "100px";
  k.style.opacity = "0.1"

}
//--------------------------------------
//BARWADIH FONT SIZE CHANGE
//----------------------------------------
var n = document.getElementById("name");
n.addEventListener("mouseover", myFunction5);
n.addEventListener("click", mySecondFunction5);
n.addEventListener("mouseout", myThirdFunction5);

function myFunction5() {
  n.style.fontSize = "95px";
  n.style.fontFamily = "Arial, Helvetica, sans-serif"
}
function mySecondFunction5() {
  n.style.fontSize = "95px";
  n.style.fontFamily = "Arial, Helvetica, sans-serif"
}

function myThirdFunction5() {
  n.style.fontSize = "100px";
  n.style.fontFamily = "'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif"
}
