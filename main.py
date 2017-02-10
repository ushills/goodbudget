import csv
from datetime import datetime

DATE_FORMAT = "%d/%m/%Y"

def main():
    cutoffdate = dateinput()
    newrowslist = []
    with open('TransHist.csv') as csvfile:
        transreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        try:
            for row in transreader:
                # print (row[0])
                date = checkdate(row)
                # print ('Date =', date)
                # print ('Cutoff date =', cutoffdate)
                if date > cutoffdate:
                    # print ('Date ok...appending')
                    newrowslist.append(stripname(row))
                else:
                    # print ('Date too early...skipping')
                    pass
        except:
            pass
    print (newrowslist)
    writecsv(newrowslist)

def stripname(inputrow):
    try:
        name = inputrow[1]
        name = name.split("  ")
        name = name[0]
        newrow = [inputrow[0], name, inputrow[2]]
        return newrow
    except:
        pass

def checkdate(inputrow):
    try:
        # print ('Running checkdate')
        d = inputrow[0]
        d = datetime.strptime(d, DATE_FORMAT)
        d = datetime.date(d)
        print ('Checkdate return =', d)
        return d
    except:
        print ('Checkdate failed')
        pass

def dateinput():
    d = input('Cut off date for transactions (d/m/YYYY)>')
    try:
        d = datetime.strptime(d, DATE_FORMAT)
        d = datetime.date(d)
        return d
    except:
        print ('Incorrect format...try again')

def writecsv(newrowslist):
    with open('TransHistNew.csv', 'w', newline='') as csvfile:
        transwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        transwriter.writerows(newrowslist)



main()
