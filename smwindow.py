

def find_window(text, pat):
    l = len(text)
    pat_map = {}

    for c in pat:
        if not pat_map.get(c):
            pat_map[c] = 1
        else:
            pat_map[c] += 1

    check_map = pat_map.copy()
    text_map = {}

    i = 0
    min_len = 99999999
    j = 0
    while i < l:

        if text[i] in check_map.keys():
            check_map[text[i]] -= 1
            if check_map[text[i]] == 0:
                check_map.pop(text[i])
        else:
            pass

        if not text_map.get(text[i]):
            text_map[text[i]] = 1
        else:
            text_map[text[i]] += 1

        if not check_map:
            while j < i:
                if text[j] not in pat_map.keys():
                    j += 1
                elif text_map[text[j]] > pat_map[text[j]]:
                    text_map[text[j]] -=1
                    j += 1

                else:
                    break

                print "calc", j, i
            curr_len = i - j + 1
            min_len = min(min_len, curr_len)

        print i, j, check_map, min_len

        i += 1

    return min_len


text = 'this is a test string'
pat = 'tist'

print find_window(text, pat)