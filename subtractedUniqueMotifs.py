import os
import csv


def directory_definer(PATH):
    if not os.path.exists(PATH + "/repeats/unique"):
        os.mkdir(PATH + "/repeats/unique")
    if not os.path.exists(PATH + "/repeats/subtracted"):
        os.mkdir(PATH + "/repeats/subtracted")


    EXT_4 = "frequencies_for_length_4.csv"
    subtracted_4 = motif_length1(PATH, EXT_4)

    EXT_5 = "frequencies_for_length_5.csv"
    temp_5 = motif_length1(PATH, EXT_5)
    subtracted_5 = subtract(subtracted_4, temp_5)
    csv_maker_s(subtracted_5, PATH, "subtracted_5")

    unique_4 = unique(subtracted_4, subtracted_5)
    csv_maker_u(unique_4, PATH, "unique_4")

    EXT_6 = "frequencies_for_length_6.csv"
    temp_6 = motif_length1(PATH, EXT_6)
    subtracted_6 = subtract(subtracted_5, temp_6)
    csv_maker_s(subtracted_6, PATH, "subtracted_6")

    unique_5 = unique(subtracted_5, subtracted_6)
    csv_maker_u(unique_5, PATH, "unique_5")

    EXT_7 = "frequencies_for_length_7.csv"
    temp_7 = motif_length1(PATH, EXT_7)
    subtracted_7 = subtract(subtracted_6, temp_7)
    csv_maker_s(subtracted_7, PATH, "subtracted_7")

    unique_6 = unique(subtracted_6, subtracted_7)
    csv_maker_u(unique_6, PATH, "unique_6")

    EXT_8 = "frequencies_for_length_8.csv"
    temp_8 = motif_length1(PATH, EXT_8)
    subtracted_8 = subtract(subtracted_7, temp_8)
    csv_maker_s(subtracted_8, PATH, "subtracted_8")

    unique_7 = unique(subtracted_7, subtracted_8)
    csv_maker_u(unique_7, PATH, "unique_7")

    EXT_9 = "frequencies_for_length_9.csv"
    temp_9 = motif_length1(PATH, EXT_9)
    subtracted_9 = subtract(subtracted_8, temp_9)
    csv_maker_s(subtracted_9, PATH, "subtracted_9")

    unique_8 = unique(subtracted_8, subtracted_9)
    csv_maker_u(unique_8, PATH, "unique_8")

    EXT_10 = "frequencies_for_length_10.csv"
    temp_10 = motif_length1(PATH, EXT_10)
    subtracted_10 = subtract(subtracted_9, temp_10)
    csv_maker_s(subtracted_10, PATH, "subtracted_10")

    unique_9 = unique(subtracted_9, subtracted_10)
    csv_maker_u(unique_9, PATH, "unique_9")

    EXT_11 = "frequencies_for_length_11.csv"
    temp_11 = motif_length1(PATH, EXT_11)
    subtracted_11 = subtract(subtracted_10, temp_11)
    csv_maker_s(subtracted_11, PATH, "subtracted_11")

    unique_10 = unique(subtracted_10, subtracted_11)
    csv_maker_u(unique_10, PATH, "unique_10")

    EXT_12 = "frequencies_for_length_12.csv"
    temp_12 = motif_length1(PATH, EXT_12)
    subtracted_12 = subtract(subtracted_11, temp_12)
    csv_maker_s(subtracted_12, PATH, "subtracted_12")

    unique_11 = unique(subtracted_11, subtracted_12)
    csv_maker_u(unique_11, PATH, "unique_11")

    EXT_13 = "frequencies_for_length_13.csv"
    temp_13 = motif_length1(PATH, EXT_13)
    subtracted_13 = subtract(subtracted_12, temp_13)
    csv_maker_s(subtracted_13, PATH, "subtracted_13")

    unique_12 = unique(subtracted_12, subtracted_13)
    csv_maker_u(unique_12, PATH, "unique_12")

    EXT_14 = "frequencies_for_length_14.csv"
    temp_14 = motif_length1(PATH, EXT_14)
    subtracted_14 = subtract(subtracted_13, temp_14)
    csv_maker_s(subtracted_14, PATH, "subtracted_14")

    unique_13 = unique(subtracted_13, subtracted_14)
    csv_maker_u(unique_13, PATH, "unique_13")


    EXT_15 = "frequencies_for_length_15.csv"
    temp_15 = motif_length1(PATH, EXT_15)
    subtracted_15 = subtract(subtracted_14, temp_15)
    csv_maker_s(subtracted_15, PATH, "subtracted_15")

    unique_14 = unique(subtracted_14, subtracted_15)
    csv_maker_u(unique_14, PATH, "unique_14")

    return

def motif_length1(path, ext):
    address = path + "/frequencies/" + ext
    norepeat = set()
    with open(address, 'r') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            k, v = row
            if v == '1':
                norepeat.add(k)
    return norepeat


def subtract(set1, set2):
    subtracted_motif = set()
    i = 1
    for s in set2:
        s1 = s[0:(len(s) - 1)]
        s2 = s[1:(len(s))]
        if s1 in set1:
            if s2 in set1:
                subtracted_motif.add(s)
        i = i + 1
    return subtracted_motif


def unique(set1, set2):

    unique_motif = set1
    i = 1
    for s in set2:
        s1 = s[0:(len(s) - 1)]
        s2 = s[1:(len(s))]
        if s1 in unique_motif:
            unique_motif.remove(s1)
        if s2 in unique_motif:
            unique_motif.remove(s2)
    return unique_motif


def csv_maker_u(filedata, path, filename):
    filedata = list(filedata)
    filepath = path + '/repeats/unique/' + filename + '.csv'

    with open(filepath, 'wb') as file:
        writer = csv.writer(file)
        writer.writerow(filedata)
    return

def csv_maker_s(filedata, path, filename):
    filedata = list(filedata)
    filepath = path + '/repeats/subtracted/' + filename + '.csv'
    with open(filepath, 'wb') as file:
        writer = csv.writer(file)
        writer.writerow(filedata)

    return


path = "E:/Bacteria/Bacteria"
sub_folders = (next(os.walk('E:/Bacteria/Bacteria'))[1])
i = 0
subtraction_10 = []

while i < (len(sub_folders)):
    path_final = path + "/" + sub_folders[i]
    print sub_folders[i]
    directory_definer(path_final)
    i=i+1



