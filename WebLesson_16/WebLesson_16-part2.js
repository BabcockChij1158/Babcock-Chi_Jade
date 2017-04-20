function text()
{
	var x = document.getElementById("canvas");
	canvas = x.getContext("2d");
	
	var pic = new Image();
	pic.src = "https://betanews.com/wp-content/uploads/2016/01/snow_leopard-600x400.jpg";
	
	pic.addEventListener("load", function() {canvas.drawImage(pic, 0, 0, 200, 150)}, false);//when to draw picture on page
											//where to draw image
	
}
window.addEventListener("load", text, false); //when the page load we start the text function