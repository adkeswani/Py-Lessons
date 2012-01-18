l = [1, 2, 3]
print "L is:", l

m = l
print "M is:", m

m[2] = 4
print "M is:", m
print "L is:", l

print "L's id is:", id(l)
print "M's id is:", id(m)
