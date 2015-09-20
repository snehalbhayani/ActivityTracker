import json
import urllib2
data { 'username':'snehal',	'activity_name':'a1',	'activity_datetime':'2015-09-20T08:25:38.135307Z',	'parent_activity_name':'pa1',	'activity_result':'S'}
print json.dumps(data)
req = urllib2.Request('http://localhost:8000/v1/activityrecordtracker/save_activityrecord/')
req.add_header('Content-Type', 'application/json')

response = urllib2.urlopen(req, json.dumps(data))
print response
