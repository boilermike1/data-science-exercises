largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try:
        intnum = int(num)
    except:
        print('Invalid input')
        continue
    if smallest is None:
        smallest = intnum
    elif intnum < smallest:
        smallest = intnum
    if largest is None:
        largest = intnum
    elif intnum > largest:
        largest = intnum

print("Maximum is", largest)
print("Minimum is", smallest)
