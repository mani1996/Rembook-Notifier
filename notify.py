# Rembook get list of posters
import requests
import json
import os
import sys


if len(sys.argv) < 3:
	print 'Usage: python notify.py username password'
	sys.exit(0)


user,pwd = sys.argv[1:3]

ses = requests.session()
response = ses.post('https://rembook.nitt.edu/login', data = {'username' : user, 'password' : pwd})

try:
	jsondata = json.loads(response.text.split('\n')[5][28:-1])
	try:
		fileObj = open('{}_done'.format(user), 'rw+')
	except:
		os.mknod('{}_done'.format(user))
		fileObj = open('{}_done'.format(user), 'rw+')
	exists = fileObj.read().split('\n')
	newOnes = 0
	names = []

	for entry in jsondata['notifications']:
		if 'wrote' in entry['message']:
			name =  entry['message'][:entry['message'].find('wrote')-1]
			if name not in exists and name not in names:
				fileObj.write(name+'\n')
				newOnes+=1
				names.append(name)

	print '{} new posts'.format(newOnes)
	if newOnes:
		print '{} posted'.format(','.join(names))

except Exception as e:
	print 'Exception : {}'.format(e)
finally:
	ses.close()
