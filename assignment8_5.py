fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0

lst = list()
wds = list()
for line in fh:
    line = line.rstrip()
    wds = line.split()
    try:
        if wds[0] == "From":
            count += 1
            lst.append(wds[1])
            print(wds[1])
    except:
        continue
print("There were", count, "lines in the file with From as the first word")
