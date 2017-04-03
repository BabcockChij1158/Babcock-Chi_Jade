function validate(){
	var x = document.forms.input.username.value;
	var atPos = x.indexOf("@");
	var dotPos = x.lastIndexOf(".");
	var y = document.forms.input.pword.value;
	
//we need... username@webAddress.extension
//if, the following...
	//@ is not in the string
	//@ is in the wrong place
	//there is no .com, .gov, or any other extension
	//final dot in the wrong place
	
	if(atPos < 1 || dotPos<atPos+2 || dotPos + 2 > x.length)
		alert("This is not a valid email address!")
	if(y.length < 6)
		alert("Password must be at least 6 characters...")
	if(atPos < 1 && dotPos < atPos+2 && dotPos + 2 > x.length && y.length < 6)
		alert("Both username and password are invalid!")
	else
		alert("Success!")
	}