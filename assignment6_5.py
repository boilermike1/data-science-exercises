text = "X-DSPAM-Confidence:    0.8475"

ipos = text.find(':')
piece = text[ipos+5:]
piece2 = float(piece)
print(piece2)
