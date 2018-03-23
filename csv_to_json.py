import csv
import json

csvfile = open('a1-burtin-transform.csv', 'r')
jsonfile = open('a1-burtin.json', 'w')

fieldnames = ("Bacteria", "Antibiotics", "Minimum_Inhibitory_Concentration",
              "Gram_Staining")
reader = csv.DictReader(csvfile, fieldnames)
data = []
next(reader)
for row in reader:
    row["Minimum_Inhibitory_Concentration"] = float(
        row["Minimum_Inhibitory_Concentration"])
    data.append(row)

json.dump(data, jsonfile)
