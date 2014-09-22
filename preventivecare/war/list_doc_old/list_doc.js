// This code depends on jQuery Core and Handlebars.js 


function search() {
	var api_key = 'CODE_SAMPLES_KEY_9d3608187'; // Get your API key at developer.betterdoctor.com
	
	var resource_url = 'https://api.betterdoctor.com/2014-09-12/doctors?query={query}&location=37.773%2C-122.413%2C100&user_location=37.773%2C-122.413&skip=0&limit=10&user_key=' + api_key;
	
	var query = "Cholesterol screening";
	query = $("#txtQuery").val();
	
	resource_url = resource_url.replace("{query}", encodeURIComponent(query));
	
	$.get(resource_url, function (data) {
	    // data: { meta: {<metadata>}, data: {<array[Doctor]>} }
	    var template = Handlebars.compile(document.getElementById('docs-template').innerHTML);
	    document.getElementById('content-placeholder').innerHTML = template(data);
	});
}

search();

function onSearch() {
	search();
}
