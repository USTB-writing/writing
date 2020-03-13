function judge(){
	if(/Android|webOS|iPhone|iPod|BlackBerry/i.test(navigator.userAgent)) {
    var div=document.getElementById("Tab").style.display="inline";
} else {
    var div=document.getElementById("Tab").style.display="none";
}
}