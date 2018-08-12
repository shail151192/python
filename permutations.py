def permutate(s, l, r):
    print l, r
    if l == r:
        print s
        return
    for i in xrange(l, r+1):
        print "swap"
        print i, l
        s[i], s[l] = s[l], s[i]
        permutate(s, l+1, r)
        s[i], s[l] = s[l], s[i]

st = 'abc'
s = list(st)
print s
permutate(s, 0,2)