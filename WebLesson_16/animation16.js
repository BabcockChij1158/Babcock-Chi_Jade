function mouse()
{
	var x = document.getElementById("canvas");
	canvas = x.getContext("2d");
	
	window.addEventListener("mousemove", icon, false);
	
}

function icon(e) {						//e is the position of our mouse
	canvas.clearRect(0, 0, 600, 600); //clears out the canvas by placing a clear rectange over every time
	var xPos = e.clientX;
	var yPos = e.clientY;
	canvas.fillRect(xPos-50, yPos-50, 100, 100);  //ypos and xpos moves mouse from the top left corner of the rectangle to the center since the rectangle is 100 px by 100px 
													// draws the rectangle depending on position of mouse

}

window.addEventListener("load", mouse, false);
