import re
import os

def find_counterparts(file):
	global idx_start, idx_end 
	os.chdir('/home/nitu/Downloads/Capstone/Split Cases v1.2/')
	case = open(file)
	lines = case.readlines()
	for idx, line in enumerate(lines):
		if line != '\n':
			idx_start = idx
			while lines[idx+1] != '\n':
				idx += 1
			idx_end = idx
		break  # get the lines with title

	title = ''
	for i in range(idx_start, idx_end+1):
		title = title + lines[i]
			
	title = title.replace('\n',' ')
	title = title.strip()
	title = re.sub(' +', ' ', title)
	title = re.sub(',', '', title) # concatenate the title lines and make it clean

	title = re.sub(' v| ag', 'key', title)
	idx_end = title.find('key')
	title1 = title[:idx_end].strip() # get the first counterpart in title

 
	idx_start = title.find('. ', idx_end)
	title2 = title[idx_start + 2:].strip() # get the second counterpart in title

	
	if ' Defendant' in title1 or ' Appellee' in title1:
		if 'Counterclaim Defendant' not in title1: 
			s = title1
			title1 = title2
			title2 = s  # make sure which counterpart is defendant and which counterpart is plaintiff 

	title1 = re.sub('Plaintiff|Petitioner|Appellant', 'key', title1)
	idx_end = title1.find('key')
	title1 = title1[:idx_end]
	counterpart1 = title1 # get those companies who are plaintiffs


	title2 = re.sub('Defendant|Appellee', 'key', title2)
	idx_end = title2.find('key')
	title2 = title2[:idx_end]
	counterpart2 = title2 # get those companies who are defendants

	case.close()
	return (counterpart1, counterpart2)
	

counterparts2 = open('counterparts2.txt', 'w')
directory = '/home/nitu/Downloads/Capstone/Split Cases v1.2/'
for filename in os.listdir(directory):
	if filename.endswith('.txt'): 
		casenumber = str(re.findall('_(\d+)_',filename)[0])
		counterparts2.write(str(casenumber) + ',' + str(find_counterparts(filename)[0])+ '\n')	
counterparts2.close()
