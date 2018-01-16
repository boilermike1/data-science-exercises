fname = input("Enter file name: ")
fh = open(fname)
nums = 0
counter = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    nums += float(line[-7:-1])
    counter += 1
print("Average spam confidence", nums / counter)
