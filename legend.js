var cb=false;

function openLeg() {
    document.getElementById("sideLegend").style.width = "230px";
}

function closeLeg() {
    document.getElementById("sideLegend").style.width = "0";
}

function toggleCB(){
	classes=["red","orange","yellow","green"]
	if (cb==false){
		//colours = ["#FF0000","#939393","#cbcbcb","#e2e2e2"]
		colours = ["rgb(0,114,178)","rgb(213,94,0)","rgb(230,159,0)","rgb(240,228,66)"]
		for (var i = 0; i<classes.length;i++){
			instances = document.getElementsByClassName(classes[i])
			for (var j = 0; j < instances.length; j++){
				instances[j].style.backgroundColor=colours[i];
			}
		}
		cb=true;
	}else {
		colours = ["#ffb3ba","#ffdfba","#ffffba","#baffc9"]
		for (var i = 0; i<classes.length;i++){
			instances = document.getElementsByClassName(classes[i])
			for (var j = 0; j < instances.length; j++){
				instances[j].style.backgroundColor=colours[i];
			}
		}
		cb=false;
	}
}