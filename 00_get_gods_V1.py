import csv

file = open("")
all_gods = list(csv.reader(file, delimiter=","))
file.close()

# remove first row
all_gods.pop(0)

# get the first 50 rows
print(all_gods[:50])

print("length: {}".format(len(all_gods)))