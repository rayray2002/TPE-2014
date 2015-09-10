function init() {
    console.log("init");
    $.get( "/control?state=init" );
	poll();
}
function forward() {
    console.log("forward");
    $.get( "/control?state=forward" );
}

function backward() {
    console.log("backward");
    $.get( "/control?state=backward" );
}

function stop() {
    console.log("stop");
    $.get( "/control?state=stop" );
}

function right() {
    console.log("right");
    $.get( "/control?state=right" );
}

function left() {
    console.log("left");
    $.get( "/control?state=left" );
}

function up() {
    console.log("up");
    $.get( "/control?state=up" );
}

function down() {
    console.log("down");
    $.get( "/control?state=down" );
}

function power(p) {
    console.log("power");
    $.get( "/control?state=power" + p);
}



var light_flag = false;
function light() {
	if(light_flag) {
		set_light_state(0);
		$.get( "/control?state=light_off" );
	} else {
		set_light_state(1);
		$.get( "/control?state=light_on" );
	}
}

function set_light_state(flag) {
	light_flag = flag;
	
	if(light_flag == 1) {
		console.log("light_on");
		$('#light').children().first().attr("src", "images/light_on.png");
	} else {
		console.log("light_off");
		$('#light').children().first().attr("src", "images/light_off.png");
	}  
}

var camera_flag = false;
function camera() {
	if(camera_flag == 1) {
		set_camera_state(0);
		$.get( "/control?state=camera_off" );
		
	} else {
		set_camera_state(1);
		$.get( "/control?state=camera_on" );
		console.log("camera_on");
	}  
}

function set_camera_state(flag) {
	camera_flag = flag;
	
	if(camera_flag == 1) {
		console.log("camera_on");
		$('#camera').children().first().attr("src", "images/camera_on.png");
	} else {
		console.log("camera_off");
		$('#camera').children().first().attr("src", "images/camera_off.png");
	}  
}

function poll() {
	console.log("poll");
	$.ajax({
		dataType: "json",
		url: "/poll",
		data: {},
		success: function(data) {
			console.log("poll data.roll" + data.roll);
			roll = data.roll;
			pitch = data.pitch;
			yaw = data.yaw;
			if(light_flag != data.light) set_light_state(data.light);
			if(camera_flag != data.camera) set_camera_state(data.camera);
			
		}
	});
	setTimeout(poll, 2000);
}

var pitch = 0.0;
var roll = 0.0;
var yaw = 0.0;
