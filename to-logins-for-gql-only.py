import sys, datetime, time
import csv

f = open('logins-only.csv', 'wb')

with open('top-users-final.csv', 'rb') as source_csvfile:
    usersReader = csv.reader(source_csvfile, delimiter=',', quotechar='\'')
    for row in usersReader:
        f.write(row[0]+', ')

#outputter.close()
source_csvfile.close()
f.close()