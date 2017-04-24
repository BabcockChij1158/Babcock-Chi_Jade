function drag(){
	taco = document.getElementById("taco");
	leftbox = document.getElementById("leftBox");
	
	taco.addEventListener("dragstart", startDrag, false);//dragstart will run the function startDrag when page loads
	taco.addEventListener("dragend", endDrag, false);
	
	
	
	leftbox.addEventListener("dragenter", dragEnter, false);//e = event = draging image into left box, when I drag into the left box, will clear the browser default functions
	leftbox.addEventListener("dragleave", dragLeave, false);
	leftbox.addEventListener("dragover", function(e){e.preventDefault()}, false);
	leftbox.addEventListener("drop", drop, false);	
	
	
}

function startDrag(e) {
	var pic = '<img id = "taco" src = "http://www.91x.com/wp-content/uploads/2016/02/taco-recipe.jpg">';
	e.dataTransfer.setData('Picture', pic);//transfers image data from one box to the next

}

function dragEnter(e){
	e.preventDefault();
	leftbox.style.background = "#8BDBDB";//#i like this one : #7F7FFF
	leftbox.style.border = "3px solid #007F7F";
}

function dragLeave(e){
	e.preventDefault();
	leftbox.style.background = "white";
	leftbox.style.border = "3px solid #67B5A3";
}

function drop(e) {
	e.preventDefault();
	leftbox.innerHTML = e.dataTransfer.getData('Picture');//html that exists in left box
}

function endDrag(e){
		pic = e.target;//pic = the dragging of the image
		pic.style.visibility = "hidden";
	
}
window.addEventListener("load", drag, false); //as window loads, will run drag, and another set of event listeners



















