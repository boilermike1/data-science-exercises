score = input('Enter Score: ')
try:
    numscore = float(score)
except:
    print('Please enter a number between 0 and 1')
    quit()

if numscore < 0 or numscore > 1:
    print('Please enter a number between 0 and 1')
elif numscore >= 0.9:
    print('A')
elif numscore >= 0.8:
    print('B')
elif numscore >= 0.7:
    print('C')
elif numscore >= 0.6:
    print('D')
else:
    print('F')
