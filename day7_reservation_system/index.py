import csv
with open('eggs.csv', 'w',  newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['spam'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['spam', 'lovely spam', 'wonderful spam'])



with open('eggs.csv', 'w',  newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(', '.join(row))