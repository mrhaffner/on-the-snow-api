import csv
from slugify import slugify

f = open('resorts_raw.csv')
csv_f = csv.reader(f)

with open('resorts.csv', 'w') as f2:
    writer = csv.writer(f2)
    for row in csv_f:
        if row[0] != 'id':
            row[0] = slugify(row[1])
        writer.writerow(row)


f.close()
f2.close()