import os

def passFiles():
	#Get all files from downloaded folder and pass to renameFile() to be corrected
	for file in os.listdir('/Users/blairjackson/PycharmProjects/LeadAdvantage/downloadedFiles'):
		if file[0] == '.':
			pass
		else:
			renameFile(file)

def renameFile(filename):
	#filename = 'EDGE_TECH_ACADEMY_COMMERCIAL_2_DATABASE_191118_191125_09172555.DAT'
	with open('downloadedFiles/' + filename, 'r') as readFile:
		with open('fixedFiles/' + filename[:-4] + '.csv', 'w+') as writeFile:
			for line in readFile:
				newline = line.split('","')
				for i, item in enumerate(newline):
					item = item.replace(',', ' ')
					item = item.replace('"', '')
					# i = i.replace(',', ' ')
					newline[i] = item
				writeFile.write(','.join(newline))