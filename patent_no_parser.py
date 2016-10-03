import os
import re
import csv

# run script one level above directory of files and pass name of folder with files
def patent_nos(directory):
    lookup = ['Patent No.', 'Patent Nos.', 'Patent no.', 'Patent nos.']
    patents = []
    no_pat_count = 0
    no_pat_files = []
    file_count = 0
    mult_count = 0
    filename_with_patents = []
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            with open(directory + '/' + filename) as File:  # opens all the text file in the directory
                file_count += 1
                content = File.readlines()
                for idx, line in enumerate(content):

                    # handle cases where patent no. wraps to next line
                    if idx != len(content) - 1:
                        check_line = line.strip() + content[idx + 1].strip()
                    else:
                        check_line = line

                    # only check cases with the word patent in either the same or preceding line
                    if any(x in check_line for x in ['Patent', 'patent']):
                        # match the patent number format
                        patents.extend(re.findall("\d[,]\d{3}[,]\d{3}", check_line))

                        # match the patent numbers without commas
                        patents.extend(re.findall("\d{7}", check_line))

                        # matches design patents of format "D###,###" with and "D######" without commas
                        patents.extend(re.findall("[D]\d{3}[,]\d{3}", check_line))
                        patents.extend(re.findall("[D]\d{6}", check_line))

                        # matches reissued patents w/ and w/out commas
                        patents.extend(re.findall("[RE]\d{2}[,]\d{3}", check_line))
                        patents.extend(re.findall("[RE]\d{5}", check_line))

                        # matches plant patents w/ and w/out commas
                        patents.extend(re.findall("[PP]\d{2}[,]\d{3}", check_line))
                        patents.extend(re.findall("[PP]\d{5}", check_line))

                if len(patents) > 1:
                    mult_count += 1
				
				# save the filename and unique set of patents found in the file
                if patents:
                    filename_with_patents.append((filename, list(set(patents))))
                # output 0 in place of patent list if no patent is found
                else:
                    filename_with_patents.append((filename, 0))
                    no_pat_count += 1
                    no_pat_files.append(filename)
                # reset patents list for next file
                patents = []

    
    # returns a list of tuples where first element of tuple is filename and second element is list of patent numbers
    return filename_with_patents


output = patent_nos('Test')

with open('patent_numbers.csv', 'wb') as f:
    writer = csv.writer(f)
    # outputs the case_id and list of corresponding patent numbers to a csv file. 0 if no patent found
    for row in output:
        writer.writerows([[row[0].split('_')[1],row[1]]])
