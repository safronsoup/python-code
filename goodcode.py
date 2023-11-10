# fibonacci sequence

# starting values

term1 = 0
term2 = 1
count = 0
totalterms = 20

# loop until we hit our total
while count < totalterms:
    print(term1)

    # update the value with each cycle
    nextterm = term1 + term2
    term1 = term2
    term2 = nextterm
    count = count + 1