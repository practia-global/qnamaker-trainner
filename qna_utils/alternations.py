# -*- coding: utf-8 -*-

import http.client, urllib.parse, json, time

# **********************************************
# *** Update or verify the following values. ***
# **********************************************

# Replace this with a valid subscription key.
subscriptionKey = 'a94165299716412686090179ccfaf7de'

host = 'westus.api.cognitive.microsoft.com'
service = '/qnamaker/v4.0'
method = '/alterations/'

def pretty_print (content):
# Note: We convert content to and from an object so we can pretty-print it.
	return json.dumps(json.loads(content), indent=4)

def get_alterations (path):
	print ('Calling ' + host + path + '.')
	headers = {
		'Ocp-Apim-Subscription-Key': subscriptionKey,
	}
	conn = http.client.HTTPSConnection(host)
	conn.request ("GET", path, '', headers)
	response = conn.getresponse ()
	return response.read ()

path = service + method
result = get_alterations (path)
print (pretty_print(result))