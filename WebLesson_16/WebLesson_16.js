function text()
{
		var x = document.getElementById("canvas");
		canvas = x.getContext("2d");
		
		canvas.shadowOffsetX = 4;//shadow set right
		canvas.shadowOffsetY = 4;//shadow set down
		canvas.shadowBlur = 6;//blur
		canvas.shadowColor = "rgba(0, 0, 255, 0.5";//rbg alpha, 255=blue, 0.5=transparency
		
		
		canvas.font = "bold 36px Tahoma";
		canvas.textAlign = "end";
		canvas.save();
		canvas.fillText("Jade", 300, 100);
		

		
		canvas.translate(100, 150);				//moves original canvas right by 100, down 15
		canvas.fillText("after translate", 300, 100);
		
												//canvas.rotate(1); moves in radians
		canvas.rotate(180* Math.PI/180); 		//built in function, can enter # degrees want to rotate
		canvas.fillText("after rotate", 0, 0);

		canvas.restore();
		canvas.scale(1.5, 4);					//wider by 1.5, taller by 4 times
		canvas.fillText("after scale", 300, 100);
}

window.addEventListener("load", text, false);