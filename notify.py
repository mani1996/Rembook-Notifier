# Rembook get list of posters
import requests
import json
import os

user = 'roll number'
pwd = 'password'

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
			if name not in exists:
				fileObj.write(name+'\n')
				newOnes+=1
				names.append(name)

	print '{} new posts'.format(newOnes)
	if newOnes:
		print '{} posted'.format(','.join(names))

except Exception as e:
	print 'Exception : {}'.format(e)
