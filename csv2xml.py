import sys

for arg in sys.argv:
    fileName = arg

import csv
with open( fileName, "rb") as f:
    reader = csv.reader(f)
    headers = reader.next()

#create XML file
with open( fileName + ".xml", 'w+') as the_file:
    the_file.write( '<?xml version="1.0" encoding="UTF-8"?>\n' )
    the_file.write('<catalog>\n')

with open(fileName) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        with open( fileName + ".xml", 'a') as the_file:
            the_file.write('\t<row>\n')
        i = 0
        while i < len(headers):
            print(headers[i])
            with open( fileName + ".xml", 'a') as the_file:
                the_file.write('\t\t<' + headers[i] + '>')
                the_file.write( row[headers[i]] )
                the_file.write('</' + headers[i] + '>\n')
            i += 1
        with open( fileName + ".xml", 'a') as the_file:
            the_file.write('\t</row>\n')

#close XML file
with open( fileName + ".xml", 'a') as the_file:
    the_file.write('</catalog>')
