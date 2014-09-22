import json
import httplib
import urlparse
import sys

# change these to your server and credentials
Url = 'http://aws-eehr-11.4.1.unitysandbox.com'
Svc_username = 'Kenne-Preventive-test'
Svc_password = 'K%nN%tHng72868'
Appname      = 'KennethNg.PreventiveHealthcare.TestApp'
Ehr_username = 'demo'

# *******************************************************************************************************
# * NAME:        UnityHelloWorldPM.py
# *
# * DESCRIPTION: Example Python application code to illustrate basic usage of Unity with Allscripts
# *              Practice Management.
# *
# * Unpublished (c) 2014 Allscripts Healthcare Solutions, Inc. and/or its affiliates. All Rights Reserved.
# *
# * This software has been provided pursuant to a License Agreement, with Allscripts Healthcare Solutions,
# * Inc. and/or its affiliates, containing restrictions on its use. This software contains valuable trade
# * secrets and proprietary information of Allscripts Healthcare Solutions, Inc. and/or its affiliates
# * and is protected by trade secret and copyright law. This software may not be copied or distributed
# * in any form or medium, disclosed to any third parties, or used in any manner not provided for in
# * said License Agreement except with prior written authorization from Allscripts Healthcare Solutions,
# * Inc. and/or its affiliates. Notice to U.S. Government Users: This software is "Commercial Computer
# * Software."
# *
# * This is example code, not meant for production use.
# *******************************************************************************************************


# build Magic action JSON string
def buildjson(action, appname, ehruserid, patientid, unitytoken,
              param1='', param2='', param3='', param4='', param5='', param6='', data='null'):
    return json.dumps({'Action': action,
                       'Appname': appname,
                       'AppUserID': ehruserid,
                       'PatientID': patientid,
                       'Token': unitytoken,
                       'Parameter1': param1, 'Parameter2': param2, 'Parameter3': param3,
                       'Parameter4': param4, 'Parameter5': param5, 'Parameter6': param6,
                       'Data': data})

# post action JSON to MagicJson endpoint, get JSON in return
def unityaction(jsonstr):
    u = urlparse.urlparse(Url)

    if (u.scheme == 'http'):
        conn = httplib.HTTPConnection(u.hostname)
    elif (u.scheme == 'https'):
        conn = httplib.HTTPSConnection(u.hostname)

    conn.request('POST', '/UnityPM/UnityService.svc/json/MagicJson',
             jsonstr,
             {'Content-Type': 'application/json'})

#    print "URL:"
#    print Url
#    print "Json str"
#    print jsonstr


    resp = conn.getresponse( )
    retjson = resp.read( ).decode( )
    conn.close( )
    return retjson

# get Unity security token from GetToken endpoint
def gettoken(username, password):
    u = urlparse.urlparse(Url)

    if (u.scheme == 'http'):
        conn = httplib.HTTPConnection(u.hostname)
    elif (u.scheme == 'https'):
        conn = httplib.HTTPSConnection(u.hostname)

    conn.request('POST', '/UnityPM/UnityService.svc/json/GetToken',
             json.dumps({'Username': username, 'Password': password}),
             {'Content-Type': 'application/json'})
    response = conn.getresponse( )
    t = response.read( ).decode( )
    conn.close( )
    return t

# Get Unity security token
token = gettoken(Svc_username, Svc_password)
print('Using Unity security token: ' + token)

# Call GetServerInfo Magic action; patient ID, Parameter1-6, and data not used
jsonstr = buildjson('GetServerInfo', Appname, Ehr_username, '', token)
unity_output = unityaction(jsonstr)

#print('Output from GetServerInfo: ')
#print(json.dumps(json.loads(unity_output), indent=4, separators=(',', ': ')))

# -----------


# Call GetPatientDemographics Magic action; Parameter1-6 and data not used for this example
#     patient = input('Enter a Patient ID to display (e.g., 72): ')
#location = input('Enter a location (e.g., 22): ')
patient = '72'

if patient.strip( ) == '':
    print('No patient ID specified; exiting.')
    sys.exit(0)

# Get patient info
jsonstr = buildjson('GetPatientDemographics', Appname, Ehr_username, patient, token)
unity_output = unityaction(jsonstr)
#print('Output from GetPatientDemographics: ')
#print(json.dumps(json.loads(unity_output), indent=4, separators=(',', ': ')))

# Remove all patient's appointments
appointmentId = '367'
dateStr = '9/21/2014'
AppStatus = 'X'

jsonstr = buildjson('SetAppointmentStatus', Appname, Ehr_username, patient, token, appointmentId, AppStatus, dateStr)
unity_output = unityaction(jsonstr)
print('Output from Schedules for this patient: ')
print(json.dumps(json.loads(unity_output), indent=4, separators=(',', ': ')))

# Get patient 's appointments
jsonstr = buildjson('GetScheduleByPatientID', Appname, Ehr_username, patient, token)
unity_output = unityaction(jsonstr)
print('Output from Schedules for this patient: ')
print(json.dumps(json.loads(unity_output), indent=4, separators=(',', ': ')))





