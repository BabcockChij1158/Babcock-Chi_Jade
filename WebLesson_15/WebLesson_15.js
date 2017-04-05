function shapes()
{
	var x = document.getElementById("canvas"); //canvas is a container
	//get allows us to use things that will enable to draw on the canvas
	canvas = x.getContext("2d");
	//canvas.strokeStyle = "yellow";
	//canvas.fillStyle = "purple";
	canvas.beginPath();
	canvas.moveTo(50, 50);
	canvas.lineTo(70, 250);
	canvas.lineto(300, 200);
	canvas.closePath();
	canvas.stroke();
	//canvas.fill();
	
}

window.addEventListener("load", shapes, false);
