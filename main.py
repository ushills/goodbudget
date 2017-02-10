import csv
from datetime import datetime

DATE_FORMAT = "%d/%m/%Y"

def main():
    # get the cut off date for transactions that
    # we want to exclude
    cutoffdate = dateinput()
    newrowslist = []

    # Open the csv file, check the dates are valid,
    # reduce the name and recombine to the newrowslist
    # variable to be written as a new csv file
    with open('TransHist.csv') as csvfile:
        transreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        try:
            for row in transreader:
                # get the date from the row
                date = checkdate(row)
                # if the date is greater than the cutoffdate
                # run the stripname function and add to the
                # newrowslist
                if date >= cutoffdate:
                    newrowslist.append(stripname(row))
                else:
                    pass
        except:
            pass

    # now we have the newrowslist, write this to a new csv file
    writecsv(newrowslist)

def stripname(inputrow):
    try:
        # extract the name from the row
        name = inputrow[1]
        # strip the extra information
        name = name.split("  ")
        name = name[0]
        # recombine to create a new correct row
        newrow = [inputrow[0], name, inputrow[2]]
        return newrow
    except:
        pass

def checkdate(inputrow):
    try:
        # extract the date information from the row and
        # convert it to datetime format
        d = inputrow[0]
        d = datetime.strptime(d, DATE_FORMAT)
        d = datetime.date(d)
        return d
    except:
        pass

def dateinput():
    d = input('Enter the cut off date for transactions (d/m/YYYY)> ')
    try:
        d = datetime.strptime(d, DATE_FORMAT)
        d = datetime.date(d)
        return d
    except:
        print ('Incorrect format...try again')

def writecsv(newrowslist):
    # write the newrowslist to the csv file
    # TransHistNew.csv
    with open('TransHistNew.csv', 'w', newline='') as csvfile:
        transwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        transwriter.writerows(newrowslist)


main()
