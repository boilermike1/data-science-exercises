import re
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "regex_sum_51582.txt"
fh = open(fname)
y = list()
for line in fh:
    y.append(re.findall('[0-9]+',line))
sumtotal = 0
counter = 0
for j in y:
    if len(j) > 0:
        for i in j:
            sumtotal += int(i)
            counter += 1
print("There are " + str(counter) + " numbers, which sum to " + str(sumtotal))
