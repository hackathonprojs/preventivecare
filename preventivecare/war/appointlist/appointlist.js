// This code depends on jQuery Core and Handlebars.js 

//var api_key = 'CODE_SAMPLES_KEY_9d3608187'; // Get your API key at developer.betterdoctor.com
//var resource_url = 'https://api.betterdoctor.com/2014-09-12/specialties?skip=0&limit=20&user_key=' + api_key;

// All keys for allscript
var Url = 'http://aws-eehr-11.4.1.unitysandbox.com'
var Svc_username = 'Kenne-Preventive-test'
var Svc_password = 'K%nN%tHng72868'
var Appname      = 'KennethNg.PreventiveHealthcare.TestApp'
var Ehr_username = 'demo'

var resource_url = 'http://aws-eehr-11.4.1.unitysandbox.com'
var json = '{"Parameter5": "", "Parameter4": "", "Parameter6": "", "Parameter1": "", "Parameter3": "", "Appname": "KennethNg.PreventiveHealthcare.TestApp", "AppUserID": "", "Token": "21FFA301-202D-46ED-B122-4533D4EFFDAD", "Action": "GetResources", "Parameter2": "", "PatientID": "", "Data": "null"}'


$.get(resource_url, function (data) {
    // data: { meta: {<metadata>}, data: {<array[Specialty]>} }
    var template = Handlebars.compile(document.getElementById('specialties-template').innerHTML);
    document.getElementById('content-placeholder').innerHTML = template(data);
});

var data = 
{"data": {
    "debug": "on",
    "window": {
        "title": "Sample Konfabulator Widget",
        "name": "main_window",
        "width": 500,
        "height": 500
    },
    "image": { 
        "src": "Images/Sun.png",
        "name": "sun1",
        "hOffset": 250,
        "vOffset": 250,
        "alignment": "center"
    },
    "text": {
        "data": "Click Here",
        "size": 36,
        "style": "bold",
        "name": "text1",
        "hOffset": 250,
        "vOffset": 100,
        "alignment": "center",
        "onMouseUp": "sun1.opacity = (sun1.opacity / 100) * 90;"
    }
}}   ;

