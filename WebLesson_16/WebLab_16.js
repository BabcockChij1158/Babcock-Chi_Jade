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
		
	var pic = new Image();
	pic.src = "https://betanews.com/wp-content/uploads/2016/01/snow_leopard-600x400.jpg";
	
	pic.addEventListener("load", function() {canvas.drawImage(pic, xPos-100, yPos-100, 200, 200)}, false);//when to draw picture on page
											//where to draw image
}

window.addEventListener("load", mouse, false);
	

	
	
	
	

