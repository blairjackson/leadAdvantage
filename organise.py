import os, pysftp

def organiseFiles():
    for file in os.listdir('/Users/aaronjones/Scripts/leadAdvantage/fixedFiles'):
    	with open('LeadAdvantageCredentialsTest', 'r') as credentials:
    		sortname = file.split('_')
    		for line in credentials:
    			match = line.split(',')
    			if sortname[0].lower() == match[0]:
    				sendFile(file, line)
    			else:
    				pass
        
		

def sendFile(filename, credentialLine):
	credentials = credentialLine.split(',')
	host = credentials[1]
	username = credentials[2]
	password = credentials[3]
	filepath = str(credentials[4]).rstrip('\n')
	print(filename)
	print(host)
	print(username)
	print(password)
	filename = '/Users/blairjackson/PycharmProjects/LeadAdvantage/fixedFiles/' + filename
	# filename = '/Users/blairjackson/PycharmProjects/LeadAdvantage/fixedFiles/' + filename
	# os.chdir('/Users/blairjackson/PycharmProjects/LeadAdvantage/fixedFiles')

	with pysftp.Connection(host, username=username, password=password) as sftp:
		print('connected!')
		with sftp.cd(filepath):
			print("uploading...." + username)
			print("uploading via SFTP.....")
			sftp.put(filename)
			print("successfully dropped to "+ username)