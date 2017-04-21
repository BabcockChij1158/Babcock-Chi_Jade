function drag(){
	taco = document.getElementById("taco");
	leftbox = document.getElementById("leftbox");
	
	taco.addEventListener("dragstart", startDrage, false);//dragstart will run the function startDrag when page loads
	
	leftbox.addEventListener("dragenter", function(e){e.preventDefault()}, false);//e = event = draging image into left box, when I drag into the left box, will clear the browser default functions
	leftbox.addEventListener("dragover", function(e){e.preventDefault()}, false);
	leftbox.addEventListener("drop", drop, false);	
	
	
}

function startDrag(e) {
	var pic = '<img id = "taco" src = "http://www.91x.com/wp-content/uploads/2016/02/taco-recipe.jpg">';
	e.dataTransfer.setData('Picture', pic);//transfers image data from one box to the next

}

function drop(e) {
	e.preventDefault();
	leftbox.innerHTML = e.dataTransfer.getData('Picture');//html that exists in left box
}
window.addEventListener("load", drag, false); //as window loads, will run drag, and another set of event listeners