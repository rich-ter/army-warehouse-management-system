/*
Template Name: HUD DJANGO - Responsive Bootstrap 5 Admin Template
Version: 1.0.0
Author: Sean Ngu
Website: http://www.seantheme.com/hud-django/
*/

var handleCheckTime = function(i) {
	"use strict";
	
	if (i < 10) {i = "0" + i};
	return i;
};
		
var handleStartTime = function() {
	"use strict";
	
	var today = new Date();
	var h = today.getHours();
	var m = today.getMinutes();
	var s = today.getSeconds();
	var a;
	m = handleCheckTime(m);
	s = handleCheckTime(s);
	a = (h > 11) ? 'pm' : 'am';
	h = (h > 12) ? h - 12 : h;
	document.getElementById('time').innerHTML = h + ":" + m + a;
	var t = setTimeout(handleStartTime, 500);
};
		
$(document).ready(function() {
	handleStartTime();
});