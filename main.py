import csv

newrowslist = []
with open('TransHist.csv', 'r') as csvfile:
    transreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    try:
        for row in transreader:
            name = row[1]
            name = name.split("  ")
            name = name[0]
            newrow = [row[0], name, row[2]]
            newrowslist.append(newrow)
    except:
        pass

with open('TransHistNew.csv', 'w', newline='') as csvfile:
    transwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
    transwriter.writerows(newrowslist)
