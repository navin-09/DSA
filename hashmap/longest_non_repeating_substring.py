def longest_non_repeating_substring(stri):
    i = 0
    res = set()
    count = 0
    j = 0
    for idx,v in enumerate(stri):
        if v in res:
            while v in res:
                res.remove(stri[i])
                i+=1
        res.add(v)
        if count < len(res):
            j = idx
            count  = len(res)
    return count, stri[i:j+1]

stri = 'abccdbas'
print(longest_non_repeating_substring(stri))