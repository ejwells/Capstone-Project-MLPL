from itertools import islice

# Function to split the large litigation file into individual cases per file
def split_cases(filename):
    count = 0
    split_lines = []
    vs = [' v. ', ' vs. ', ' v.']
    lookup = ['Plaintiff', 'Appellant', 'Petitioner']

    # open file
    with open(filename) as File:
        content = File.readlines() # create a list where each line from the file is a new element
        num_lines = [3,4]
        for idx, line in enumerate(content): # this loops through each line in the content list
            # figure out how many blank lines are in a row
            if line == '\n':
                count += 1
            else:
                count = 0

            if count in num_lines: # if there are 3 or 4

                if any(x in content[idx + 1] for x in lookup) or any(x in content[idx + 2] for x in lookup):

                    if any(x in content[idx + 1] for x in vs):
                        split_lines.append(idx)
                        continue
                    if any(x in content[idx + 2] for x in vs):
                        split_lines.append(idx)

        # remove duplicates from split lines
        for idx, val in enumerate(split_lines):
            if val - split_lines[idx - 1] == 1:
                del split_lines[idx - 1]

        # this segment splits the litigation file at each recorded index and puts the cases in their own text file
        # the name of the cases has the case number and the line number they begin at in the large file
        x = 0
        for idx, val in enumerate(split_lines):
            # save each case file with it's file ID and line number in large litigation file
            thefile = open('file_' + str(idx) + '_' + str(val) + '.txt', 'w')

            for item in islice(content, x, val):
                thefile.write("%s" % item)
            thefile.close()
            last_val = val
            x = val + 1

split_cases('litigation.txt') #12,324 files

import os
def outcomes(directory):
    lookup = 'OUTCOME:'
    Storage = []
    for filename in os.listdir(directory):
        if filename.endswith('.txt'): 
            with open(directory + '/' + filename) as File: #opens all the text file in the directory
                start_passage = None
                reading = File.readlines()
                for num, line in enumerate(reading):
                    if lookup in line:                     #iterates line by line and looks for the lookup string
                        start_passage = num
                if start_passage != None:                  #only executes if lookup is found
                    replaceblank = reading[start_passage:] #getting the index where lookup field is. 
                    for n, i in enumerate(replaceblank):             #I need to find the next empty line.
                        if i == '\n':
                            replaceblank[n] = None                   #Empty lines are stored as \n I am now making them empty 
                    for num, line in enumerate(replaceblank):
                        if replaceblank[num] == None:
                            end_passage = num                #Determining the index of the empty line and storing it
                            break
                    Joined = ' '.join(map(str.rstrip, replaceblank[:end_passage]))  #Combining everything from start to none and removing \n in this dataset
                    Storage.append((filename,Joined))          #Storing it in storage
                else:                                      #if lookup not found add this to Storage list
                    Insert = 'No OUTCOME field in this CASE.'
                    Storage.append((filename,Insert))
    return Storage
                
OUTCOME = outcomes('Files')

with open ("OUTCOMES.txt","w")as fp:
    for filename, information in OUTCOME:
        fp.write("\n".join(["%s %s" % (filename, information)]) + "\n")
		
		import os
def judges(directory):
    lookup = 'JUDGES:'
    Storage = []
    for filename in os.listdir(directory):
        if filename.endswith('.txt'): 
            with open(directory + '/' + filename) as File:      #opens all the text file in the directory
                start_passage = None
                reading = File.readlines()
                for num, line in enumerate(reading):
                    if lookup in line:                     #iterates line by line and looks for the lookup string
                        start_passage = num
                if start_passage != None:                              #only executes if lookup is found
                    total_size = len(reading)
                    replaceblank = reading[start_passage:total_size]   #getting the index where lookup field is. 
                    for n, i in enumerate(replaceblank):               #I need to find the next empty line.
                        if i == '\n':
                            replaceblank[n] = None       #Empty lines are stored as \n I am now making them empty 
                    for num, line in enumerate(replaceblank):
                        if replaceblank[num] == None:
                            end_passage = num            #Determining the index of the empty line and storing it
                            break
                    Joined = ' '.join(map(str.rstrip, replaceblank[:end_passage]))    #Combining everything from start to none and removing \n in this dataset
                    Storage.append((filename,Joined))  #Storing it in storage
                else:                       #if lookup not found add this to Storage list
                    Insert = 'No JUDGES field in this CASE.'
                    Storage.append((filename,Insert))
    return Storage
                
JUDGE = judges('Test')

with open ("JUDGES.txt","w")as fp:
    for filename, information in JUDGE:
        fp.write("\n".join(["%s %s" % (filename, information)]) + "\n")
		
		import os
def counsel(directory):
    lookup = 'COUNSEL:'
    Storage = []
    for filename in os.listdir(directory):
        if filename.endswith('.txt'): 
            with open(directory + '/' + filename) as File:      #opens all the text file in the directory
                start_passage = None
                reading = File.readlines()
                for num, line in enumerate(reading):
                    if lookup in line:                     #iterates line by line and looks for the lookup string
                        start_passage = num
                if start_passage != None:                              #only executes if lookup is found
                    total_size = len(reading)
                    replaceblank = reading[start_passage:total_size]   #getting the index where lookup field is. 
                    for n, i in enumerate(replaceblank):               #I need to find the next empty line.
                        if i == '\n':
                            replaceblank[n] = None       #Empty lines are stored as \n I am now making them empty 
                    for num, line in enumerate(replaceblank):
                        if replaceblank[num] == None:
                            end_passage = num            #Determining the index of the empty line and storing it
                            break
                    Joined = ' '.join(map(str.rstrip, replaceblank[:end_passage]))    #Combining everything from start to none and removing \n in this dataset
                    Storage.append((filename,Joined))  #Storing it in storage
                else:                       #if lookup not found add this to Storage list
                    Insert = 'No COUNSEL field in this CASE.'
                    Storage.append((filename,Insert))
    return Storage
                
COUNSEL = counsel('Test')

with open ("COUNSEL.txt","w")as fp:
    for filename, information in COUNSEL:
        fp.write("\n".join(["%s %s" % (filename, information)]) + "\n")
		
		import os
def case_summary(directory):
    lookup = 'CASE SUMMARY:'
    Storage = []
    for filename in os.listdir(directory):
        if filename.endswith('.txt'): 
            with open(directory + '/' + filename) as File:      #opens all the text file in the directory
                start_passage = None
                reading = File.readlines()
                for num, line in enumerate(reading):
                    if lookup in line:                     #iterates line by line and looks for the lookup string
                        start_passage = num
                if start_passage != None:                              #only executes if lookup is found
                    total_size = len(reading)
                    replaceblank = reading[start_passage:total_size]   #getting the index where lookup field is. 
                    for n, i in enumerate(replaceblank):               #I need to find the next empty line.
                        if i == '\n':
                            replaceblank[n] = None       #Empty lines are stored as \n I am now making them empty 
                    for num, line in enumerate(replaceblank):
                        if replaceblank[num] == None:
                            end_passage = num            #Determining the index of the empty line and storing it
                            break
                    Joined = ' '.join(map(str.rstrip, replaceblank[:end_passage]))    #Combining everything from start to none and removing \n in this dataset
                    Storage.append((filename,Joined))  #Storing it in storage
                else:                       #if lookup not found add this to Storage list
                    Insert = 'No CASE SUMMARY field in this CASE.'
                    Storage.append((filename,Insert))
    return Storage
                
CASESUMMARY = case_summary('Test')

with open ("CASESUMMARY.txt","w")as fp:
    for filename, information in CASESUMMARY:
        fp.write("\n".join(["%s %s" % (filename, information)]) + "\n")
		
	import os
def core_terms(directory):
    lookup = 'CORE TERMS:'
    Storage = []
    for filename in os.listdir(directory):
        if filename.endswith('.txt'): 
            with open(directory + '/' + filename) as File:      #opens all the text file in the directory
                start_passage = None
                reading = File.readlines()
                for num, line in enumerate(reading):
                    if lookup in line:                     #iterates line by line and looks for the lookup string
                        start_passage = num
                if start_passage != None:                              #only executes if lookup is found
                    total_size = len(reading)
                    replaceblank = reading[start_passage:total_size]   #getting the index where lookup field is. 
                    for n, i in enumerate(replaceblank):               #I need to find the next empty line.
                        if i == '\n':
                            replaceblank[n] = None       #Empty lines are stored as \n I am now making them empty 
                    for num, line in enumerate(replaceblank):
                        if replaceblank[num] == None:
                            end_passage = num            #Determining the index of the empty line and storing it
                            break
                    Joined = ' '.join(map(str.rstrip, replaceblank[:end_passage]))    #Combining everything from start to none and removing \n in this dataset
                    Storage.append((filename,Joined))  #Storing it in storage
                else:                       #if lookup not found add this to Storage list
                    Insert = 'No CORE TERMS field in this CASE.'
                    Storage.append((filename,Insert))
    return Storage
                
CORETERMS = core_terms('Test')

with open ("CORETERMS.txt","w")as fp:
    for filename, information in CORETERMS:
        fp.write("\n".join(["%s %s" % (filename, information)]) + "\n")

	from collections import Counter
filename = 'OUTCOMES.txt'
lookup = ['Judgment vacated', 'award', 'denied', 'No OUTCOME field in this CASE.', 'dismiss', 'granted', 'entered', 'reversed', 'affirmed']
data = []
with open(filename) as File:
    reading = File.readlines()
    for num, line in enumerate(reading):
        for matches in lookup:
            if matches in line:
                data.append((matches))
                
c = Counter(data)
newlist = c.items()
	
	
	import MySQLdb
def connection(organization, patent_id):
    try:
        connection = MySQLdb.connect(
            host = 'rosencrantz.berkeley.edu',
            user = 'uspto',
            passwd = 'ferrisbueller')  #Creates the connection
        #return "Success"
        cursor = connection.cursor() 
        #Gets the assigne_id
        cursor.execute("""SELECT assignee.id, assignee.name_first, assignee.name_last, assignee.organization, patent_assignee.patent_id 
                        FROM uspto.assignee 
                        INNER JOIN uspto.patent_assignee ON assignee.id = patent_assignee.assignee_id 
                        WHERE organization like %s and patent_assignee.patent_id = %s;""", 
                       ('%'+organization+'%', patent_id,))
        tables = cursor.fetchall() 
        if not tables:
            return "Patent ID does not match with organization."
        return tables
    except MySQLdb.Error:
        return "ERROR IN CONNECTION"

		
print connection("Myriad Genetics, Inc", '5693473')

import pandas as pd
df = pd.read_csv('updated_patent_DB.tsv', sep='\t', nrows=1000)