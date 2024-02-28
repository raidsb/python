def matchingStrings(strings, queries):
    # Write your code here
    str_dict = {}
    result = []
    for s in strings:
        str_dict[s] = 1 if s not in str_dict.keys() else str_dict[s] + 1
    
    for q in queries:
        r = str_dict[q] if q in str_dict.keys() else 0
        print(q, r)
        result.append(r)
    
    return result
