# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

for line in fh:
    fz = line.strip()
    fy = fz.upper()
    print(fy)
