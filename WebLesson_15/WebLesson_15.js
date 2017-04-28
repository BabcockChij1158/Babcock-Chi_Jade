function shapes()
{
	var x = document.getElementById("canvas"); //canvas is a container
	//get allows us to use things that will enable to draw on the canvas
	canvas = x.getContext("2d");
	
	
	canvas.beginPath();
	canvas.moveTo(50, 200);
	canvas.lineTo(150, 250);
	canvas.lineTo(70, 350);
	canvas.lineTo(200, 290);
	canvas.lineTo(240, 400);
	canvas.lineTo(270, 290);
	canvas.lineTo(410, 350);
	canvas.lineTo(330, 250);
	canvas.lineTo(430, 200);
	canvas.lineTo(315, 175);
	canvas.lineTo(410, 90);
	canvas.lineTo(270, 125);
	canvas.lineTo(235, 15);
	canvas.lineTo(200, 125);
	canvas.lineTo(70, 90);
	canvas.lineTo(165, 175);
	canvas.closePath();
	canvas.stroke();
	
	var g = canvas.createLinearGradient(200, 200, 250, 250);
	g.addColorStop(0, "purple");
	g.addColorStop(0.5, "white");
	g.addColorStop(1, "yellow");
	canvas.fillStyle = g;
	canvas.fill();
}

window.addEventListener("load", shapes, false);
