//odoo.define('opencv_attendance.face_detection_video', function(require) {
//"use strict";

const button = document.getElementById("button_id");
const stop_button = document.getElementById("stop_id");
const video=document.getElementById("video")
function startVideo(){
alert("function block is executing")
navigator.getUserMedia({
video:{}},
stream => video.srcObject = stream,
err => console.error(err))
}
stop_button.onclick = function vidOff() {
   const video = document.querySelector("video");

// A video's MediaStream object is available through its srcObject attribute
const mediaStream = video.srcObject;

// Through the MediaStream, you can get the MediaStreamTracks with getTracks():
const tracks = mediaStream.getTracks();

// Tracks are returned as an array, so if you know you only have one, you can stop it with:
tracks[0].stop();

// Or stop all like so:
tracks.forEach(track => track.stop())
};
//});