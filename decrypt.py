def decrypt(s, pos):
    count = 0
    i = 0
    l = len(s)
    sub = ''
    ch = ''
    while i < l:
        if ord(s[i]) >= 48 and ord(s[i]) <= 57:
            n = n * 10 + int(s[i])
            sl = len(sub)
            if count + (n*sl) > pos:
                rem = pos-count
                t= rem % sl
                if t == 0:
                    ch = sub[sl-1]
                else:
                    ch = sub[t-1]
            else:
                count += n*sl
                sub = ''
        else:
            sub += s[i]

        i += 1

    return ch


s = 'ab4c12ed3'
print decrypt(s, 21)