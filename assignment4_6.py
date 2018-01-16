def computepay(h,r):
    if h > 40:
        return 40 * r + (h - 40) * r * 1.5
    else:
        return h * r

hrs_in = input("Enter Hours:")
rate_in = input("Enter Rate:")
hrs = float(hrs_in)
rate = float(rate_in)
p = computepay(hrs,rate)
print("Pay",p)
