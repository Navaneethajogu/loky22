from collections import Counter 

name = "Navaneetha"
print(Counter(name))

##############################################
#name = "navaneetha"

def counter(name):
    d = {}
    for ch in name:
        if d.get(ch):     # if already exists
            d[ch] += 1
        else:
            d[ch] = 1
    return d

print(counter('navaneetha'))