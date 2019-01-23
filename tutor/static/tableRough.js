//Last update May 14, 2018

url = "http://127.0.01.:8000/";
//Creates the initial portion of the wepbage, creating a table
//of all current sessions created.

/*
	Needs filters implemented.
	Needs bookmark and favorite button functionality.
	Needs to save scroll location after selecting detail.
	Should include pagination.
*/
function createTable(){
		$.getJSON(url + "sessions/?format=json", function(data){
			$(".sessions").html("");
			dateTime = data.startSession
			$(data).each(function(index, value){
				elements = index + 1;
				if(index%2==1)
					bg ="rowBlue";
				else 
					bg = "";
				$(".sessions").append("<div id="+value.id+" class=\""+ bg + " sessionRow row\">\
					<div class=\"sessionRowProfilePicture\">\
						<img src =\"https://members.nationalgeographic.com/static-media/images/css_images/nationalGeographic_default_avatar.jpg\" class=\"profilePictureSessionRow\">\
					</div>\
					<div class=\"sessionRowName\">\
						<span>" + value.creator +"</span>\
					</div>\
					<div class=\"sessionRowInfo\">\
						<span>" + value.section + "</span><br>\
						<span>" + dateParser(value.startSession) +"</span>\
	                    <br>\
						<span>" + value.location + "</span>\
					</div>\
					<div class=\"sessionAction pull-right\">\
						<button type=\"button\" class=\""+ bg +" actionButton-blue\"><i class=\"fa fa-plus\"></i></button>\
						<button type=\"button\" class=\""+ bg +" actionButton-red\"><i class=\"fa fa-bookmark\"></i></button>\
					</div>"
			);
											
		});

	});
}


//Parses through the json date and turns it into something
//managebale and readable by the user.

function dateParser(dateTime){
	var parsedDate = "";

	year = dateTime.substring(0, 4);
	month = dateTime.substring(5, 7);
	day = dateTime.substring(8, 10);

	if(month = "01")
		month = "January ";
	else if(month = "02")
		month = "February ";
	else if(month = "03")
		month = "March ";
	else if(month = "04")
		month = "April ";
	else if(month = "05")
		month = "May ";
	else if(month = "06")
		month = "June ";
	else if(month = "07")
		month ="July ";
	else if(month = "08")
		month = "August ";
	else if(month = "09")
		month = "September ";
	else if(month = "10")
		month = "October ";
	else if(month = "11")
		month = "November ";
	else
		month = "December";

	if(day[1] == "1" && day[0] != "1")
		day += "st";
	else if(day[1] == "2" && day[0] != "1")
		day += "nd";
	else if(day[1] == "3" && day[0] != "1")
		day += "rd";
	else
		day += "th";

	if(day[0] == "0")
		day = day.substring(1, 4);

	parsedDate = month + day + ", " + year;
	return parsedDate;
}

$(document).ready(function(){
	var elements = 0;
	var bg = "";

	createTable();

	//Converts the session table into a detailed view of
	//the session that was clicked on, showing the creator,
	//people attending, location, title and description.

	$(".sessions").on('click', ".sessionRow", function(){
		id = (this).id;

		$.getJSON(url + "session/" + id + "?format=json", function(session){

			//upper half of the session detail page
			base = "\
			<div class=\"sessionHeader row\">\
				<div class=\"row backButton\">\
					<div><i class=\"fa fa-arrow-left\"></i></div>\
				</div>\
				<img src =\"https://members.nationalgeographic.com/static-media/images/css_images/nationalGeographic_default_avatar.jpg\" style=\"width: 10%; height: 100%;\">\
				<div class=\"creator\" style=\"padding-left: 1vw;\"></div>\
			</div>\
			<div class=\"sessionBody\">\
				<div class=\"row\">\
					<div class=\"description\">\
						<h4>" + session.title + "</h4>\
						<div class=\"section\"></div>\
						<div>" + session.description + "</div>\
					</div>\
					<div class=\"members\">\
						<div class=\"memberTitle\">Group</div>\
			"

			//creates a list of the user that are currently attending
			//increases readability by alternating color the table.
			memberIndex = 0;
			bg = "";
			members ="";
			(session.attending).forEach(function(attending){
				if(memberIndex%2 == 1)
					bg = "rowBlue";
				else 
					bg = "";
				members += "<div class=\"member " + bg + "\">\
								<div class=\"row container\">\
									<img src =\"https://members.nationalgeographic.com/static-media/images/css_images/nationalGeographic_default_avatar.jpg\" class=\"memberProfilePicture\">\
								<div style=\"padding: 1vw;\">" + attending + "</div>\
								</div>\
							</div>\
				";
				++memberIndex;
		
			});

			//The bottom half of the session  detail page, closes
			//off the divs and includes buttons for the user to interact
			//with.
			close ="<div class=\"memberAction\"> JOIN </div>\
					</div>\
				</div>\
			</div>"
			$(".sessions").html(base + members + close);
			$.getJSON(url + "profile/" + session.creator, function(creator){
				$(".creator").html("<a style=\"font-size: 1.5vw;\">" + creator.username +"</a><br>\
					<a style=\"font-size: 1vw;\">" + creator.school + "</a>");
			});
			$.getJSON(url + "section/" + session.section, function(section){
				$(".section").html("<a style=\"font-size: .9vw;\">" + section.name +  ",</a>\
					<a style=\"font-size: .9vw;\">" + section.subject + "</a>");
			});

		});

	});

	$(".sessions").on('click', ".backButton", function(){
		createTable();
	});

	//Allows the user to select the filters they want to use
	//each button will change the text fields(filters) available
	//to use.
	/*
		Filters should change the nature of the createTable function
		and change what is recieved from the json request.  This should
		be handled server side, we need views that can filter based on
		parameters in the url.
	*/

	$(".filterInstitution").on('click', function(){
		$(".sessionFilterBody").html("\
			<button class=\"inputMarker\"><i class=\"fa fa-institution\"></i></button><input placeholder=\" School\" type=\"text\" name=\"school\">\
			<button class=\"inputMarker\"><i class=\"fa fa-book\"></i></button><input placeholder=\" Subject\" type=\"text\" name=\"subject\">\
			<button class=\"inputMarker\"><i class=\"fa fa-pencil\"></i></button><input placeholder=\" Class\" type=\"text\" name=\"class\">\
			"
		);
	});
	$(".filterDateTime").on('click', function(){
		$(".sessionFilterBody").html("\
			<button class=\"inputMarker\"><i class=\"fa fa-calendar\"></i></button><input placeholder=\" Date\" type=\"text\" name=\"school\">\
			<button class=\"inputMarker\"><i class=\"fa fa-clock-o \"></i></button><input placeholder=\" Time\" type=\"text\" name=\"subject\">\
			"
			);
		});
	$(".filterDateTime").on('click', function(){
		$(".sessionFilterBody").html("\
			<button class=\"inputMarker\"><i class=\"fa fa-calendar\"></i></button><input placeholder=\" Date\" type=\"text\" name=\"school\">\
			<button class=\"inputMarker\"><i class=\"fa fa-clock-o \"></i></button><input placeholder=\" Time\" type=\"text\" name=\"subject\">\
			"
		);
	});
	$(".filterUsers").on('click', function(){
		$(".sessionFilterBody").html("\
			<button class=\"inputMarker\"><i class=\"fa fa-user\"></i></button><input placeholder=\" Creator\" type=\"text\" name=\"school\">\
			<button class=\"inputMarker\"><i class=\"fa fa-group\"></i></button><input placeholder=\" Attending\" type=\"text\" name=\"subject\">\
			"
		);
	});

	//Hides the modal that allows the user to create a 
	//new session.  

	var modal = document.getElementById('myModal');
	var btn = document.getElementById("myBtn");
	var span = document.getElementsByClassName("close")[0];
	btn.onclick = function() {
	    modal.style.display = "block";
	}
	span.onclick = function() {
	    modal.style.display = "none";
	}
	window.onclick = function(event) {
	    if (event.target == modal) {
	        modal.style.display = "none";
	    }
	}

	//dynamically changes the list of sections available based on the json
	//response.  
	/*
		Should be based off of the school selected, list has the potential 
		to become long. 

		Should become a hybrid input/dropdown box that filters as the user
		enters keys.
	*/
	$.getJSON(url + "sections/" + "?format=json", function(sections){
		$(sections).each(function(index, section){
			$(".sectionOptions").append("<option>" + section.name + "</option>");
		});
	});

	//Makes a post request given the information.
	/*
		Needs to create error handling.
		Should be modified to allow currently authenticated user to make posts,
		defaulted to specific account.
	*/
	$(".submitSession").on('click', function(){

		var title = $("#title").val();
		var school = $("#school").val();
		var section = $("#section").val();
		var description = $("#info").val();
		var datetime = $("#date").val() + "T" + $("#time").val() + ":00Z";
		var location = $("#location").val();


		var session = {
			section: section,
		    creator: "egutierrez",
		    attending: [],
		    title: title,
		    description: description,
		    startSession: datetime,
		    endSession: datetime,
		    location: location,
		}

		$.ajax({
			type: 'POST',
			url: url+ 'sessions/',
			data: session,
			dataType: "json",
			success: function()
			{
				if((elements - 1)%2 == 1)
					bg = "";
				else
					bg = "rowBlue"
				$(".sessions").prepend("<div class=\""+ bg + " sessionRow row\">\
					<div class=\"sessionRowProfilePicture\">\
						<img src =\"https://members.nationalgeographic.com/static-media/images/css_images/nationalGeographic_default_avatar.jpg\" class=\"profilePictureSessionRow\">\
					</div>\
					<div class=\"sessionRowName\">\
						<span>" + session.creator +"</span>\
					</div>\
					<div class=\"sessionRowInfo\">\
						<span>" + session.section + "</span><br>\
						<span>" + session.startSession +"</span>\
	                    <br>\
						<span>" + session.location + "</span>\
					</div>\
					<div class=\"sessionAction pull-right\">\
						<button type=\"button\" class=\""+ bg +" actionButton-blue\"><i class=\"fa fa-plus\"></i></button>\
						<button type=\"button\" class=\""+ bg +" actionButton-red\"><i class=\"fa fa-bookmark\"></i></button>\
					</div>"
				);
				++elements;
			}
		});

		modal.style.display="none";
	});
	
	

});