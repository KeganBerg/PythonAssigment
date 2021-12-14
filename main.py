from os import path
# !!!!!!!!!!!!!!!!!!Major Callab with Carly, she helped me understand dictionaries and how to make my life easier
# while being sick, shes amazing.
dataFileName = "pythonData.txt"
outputFilename = "sorted_data.txt"
HomeFolder = path.expanduser('~')

fullFileName = path.join(HomeFolder, "downloads", dataFileName)

dataProfilesUserNames = {}  # Header for the data file, that we're using to create a new list of sorted data from
# "pythonData.txt"
try:
    with open(dataFileName, 'r') as inputFile, open(outputFilename, 'w') as outputFile:
        NewList = []  # New list other that the "Was is" this is turn the new data set into sorted sort based on the
        # assignment requirements
        fileHeader = inputFile.readline()
        for newInputLine in inputFile.readlines():
            newLine = newInputLine.strip()  # removes any leading (spaces at the beginning) and trailing (spaces at
            # the end) characters (space is the default leading character to remove)
            id, first_name, last_name, email, gender, ip_address, favorite_color, ssn, buzzword, animal_name = newLine.split('\t')
            dataProfilesUsers = [animal_name, buzzword, email, favorite_color, first_name, gender, id, ip_address, last_name, ssn]
            print(dataProfilesUserNames)
            outputFile.write('\t'.join(dataProfilesUserNames) + '\n')  # output files displays new sorted data based
            # on the split replacing the new sorted file with the correct placements for the header row.
        pass
except FileNotFoundError:
    print(f"ERROR: File {fullFileName} doesn't exist! ):")
