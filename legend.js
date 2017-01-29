var cb=false; // colourblind mode

//open legend
function openLeg() {
    document.getElementById("sideLegend").style.width = "230px";
}

//close legend
function closeLeg() {
    document.getElementById("sideLegend").style.width = "0";
}

//toggle colourblind mode
function toggleCB(){
	classes=["red","orange","yellow","green"] //colour classes we are targetting
	if (cb==false){
		colours = ["rgb(0,114,178)","rgb(213,94,0)","rgb(230,159,0)","rgb(240,228,66)"] //colourblind colours
		for (var i = 0; i<classes.length;i++){
			instances = document.getElementsByClassName(classes[i]) //get list of colour class instances
			for (var j = 0; j < instances.length; j++){
				instances[j].style.backgroundColor=colours[i]; //change the colour of each instance of colour class
			}
		}
		cb=true; //set colourblind mode to true
	}else {
		colours = ["#ffb3ba","#ffdfba","#ffffba","#baffc9"] //regular colours
		for (var i = 0; i<classes.length;i++){
			instances = document.getElementsByClassName(classes[i]) //get list of colour class instances
			for (var j = 0; j < instances.length; j++){
				instances[j].style.backgroundColor=colours[i]; //change colour of each instance of colour class
			}
		}
		cb=false; //set colourblind mode to false
	}
}