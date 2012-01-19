peopleCookies = {"Adi" : 5, "Beth" : 4, "Robert" : 6, "Brad" : 4}

for p in peopleCookies.keys():
    print p, "has", peopleCookies[p], "cookies"

total = 0
for c in peopleCookies.values():
    total = total + c
print "Total cookies:", total
