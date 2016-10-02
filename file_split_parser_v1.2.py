from itertools import islice

# Function to split the large litigation file into individual cases per file
def split_cases(filename):

    count = 0
    split_lines = []
	# define identifiers
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

            if count in num_lines: # if there are 3 or 4 blank lines

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

split_cases('litigation.txt')


