def most_frequent(string):
    import operator
    d = {}
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    d_lower={k.lower:v for k, v in d.items()}
    d_sorted = dict(sorted(d.items(), key = operator.itemgetter(1),reverse = True))
    return d_sorted
s=input("Enter a String: ")
print ("Frequency of each character: " ,most_frequent(s))