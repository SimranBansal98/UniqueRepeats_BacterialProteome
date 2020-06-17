Salmonella Enterica



___________________________________________________________________________________________________________________________________

import csv
from collections import Counter

fileLines = []

with open('E:\CIC\CIC_6th sem\Sem_Long\Sal_Ent\Sal_Ent_prot.csv') as csvDataFile:   #source csv file with onl one column containing the protein sequence
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        fileLines.append(row[0])

totalProteins = len(fileLines)      #finding number of proteins from the source file

outputCSV1 = csv.writer(open('E:\CIC\CIC_6th sem\Sem_Long\Sal_Ent\output1.csv', "w"))     #output csv file, needs to be created by user before hand
outputCSV2 = csv.writer(open('E:\CIC\CIC_6th sem\Sem_Long\Sal_Ent\output2.csv', "w"))     #output csv file, needs to be created by user before hand
outputCSV3 = csv.writer(open('E:\CIC\CIC_6th sem\Sem_Long\Sal_Ent\output3.csv', "w"))     #output csv file, needs to be created by user before hand
outputCSV4 = csv.writer(open('E:\CIC\CIC_6th sem\Sem_Long\Sal_Ent\output4.csv', "w"))     #output csv file, needs to be created by user before hand
outputCSV5 = csv.writer(open('E:\CIC\CIC_6th sem\Sem_Long\Sal_Ent\output5.csv', "w"))     #output csv file, needs to be created by user before hand



n=1     #initial length of motifs

while n<=5:       #n is the length of the motif
    d = Counter()  # the main dictionary for storing the motifs
    i=0
    while i<totalProteins:   #i here is the protein number in the excel file
        protein = str(fileLines[i])
        j=0                                     #setting the initial point of start of array of characters to start finding motifs as zero
        proteinLength = len(protein)            #finding the length of the character protein array
        motifList = []
        while j<=(proteinLength - (n+1)):
            k=n
            string_protein = ""
            if (j+k)<=proteinLength:
                string_protein =  protein[j:(j+k)]      #making motifs
            motifList.append(string_protein)          #combining motifs of a particular length into a single array
            j = j+1

        temp_dict = Counter(motifList)        #making the smaller dictionaries for a certain protein for motifs of certain length

        d = d + temp_dict
        i = i+1

    if n==1:
        for key, val in d.items():
            outputCSV1.writerow([key, val])
    elif n==2:
        for key, val in d.items():
            outputCSV2.writerow([key, val])
    elif n == 3:
        for key, val in d.items():
            outputCSV3.writerow([key, val])
    elif n == 4:
        for key, val in d.items():
            if val >= 3:
                outputCSV4.writerow([key, val])
    elif n == 5:
        for key, val in d.items():
            if val >= 3:
                outputCSV5.writerow([key, val])
    else:
        print("Wrong number, improve and change conditions")
    n= n+1


_______________________________________________________________________________________________________________________________________