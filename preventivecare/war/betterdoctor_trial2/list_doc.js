// This code depends on jQuery Core and Handlebars.js 

var api_key = 'CODE_SAMPLES_KEY_9d3608187'; // Get your API key at developer.betterdoctor.com

var resource_url = 'https://api.betterdoctor.com/2014-09-12/doctors?location=37.773,-122.413,100&skip=2&limit=10&user_key=' + api_key;

$.get(resource_url, function (data) {
    // data: { meta: {<metadata>}, data: {<array[Doctor]>} }
    var template = Handlebars.compile(document.getElementById('docs-template').innerHTML);
    document.getElementById('content-placeholder').innerHTML = template(data);
});