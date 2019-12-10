//Original version spelt accordion accordian?


$(document).ready(function(){
	var video=document.getElementById("video1");
	video.addEventListener("timeupdate", function(){
		if(this.currentTime >= 30) {
			this.pause();
		}
	});
});

$('.video').click(function(){this.paused?this.play():this.pause();});