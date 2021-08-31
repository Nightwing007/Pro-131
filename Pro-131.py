import csv
import pandas as pd

rows = []

with open("Pro-131.csv","r") as f :
  csvR = csv.reader(f)
  for row in csvR :
    rows.append(row)

header = rows[0]
planetData = rows[1:]

header[0] = "Index"

temp_list = list(planetData)

for data in planetData :
  planetMass = data[3]
  if planetMass.lower() == "unknown":
    planetData.remove(data)
    continue
  planetRadius = data[4]
  if planetRadius.lower() == "unknown":
    planetData.remove(data)
    continue

for data in planetData :
    mass = float(data[3]) * 1.989e+30
    data[3] = mass
    radius = float(data[4]) * 6.957e+8
    radius[4] = radius

plM = []
plN = []
plR = []


for data in planetData :
  plM.append(data[3])
  plN.append(data[1])
  plR.append(data[4])


planetGravity = []

for index,name in enumerate(plN):
  gravity = ((float(plM[index]))/float(plR[index]) * float(plR[index]) ) * 6.674e-11
  planetGravity.append(gravity)

for index,row in enumerate(planetData) :
    row.append(planetGravity[index])

header = header.append("Gravity")

with open("final.csv","a+") as f :
    csvW = csv.writer(f)
    csvW.writerow(header)
    csvW.writerows(planetData)



