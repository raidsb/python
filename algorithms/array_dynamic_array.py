"""
Declare a 2-dimensional array, , of  empty arrays. All arrays are zero indexed.
Declare an integer, , and initialize it to .

There are  types of queries, given as an array of strings for you to parse:

Query: 1 x y
Let .
Append the integer  to .
Query: 2 x y
Let .
Assign the value  to .
Store the new value of  to an answers array.
Note:  is the bitwise XOR operation, which corresponds to the ^ operator in most languages. Learn more about it on Wikipedia.  is the modulo operator.
Finally, size(arr[idx]) is the number of elements in arr[idx]

Function Description

Complete the dynamicArray function below.

dynamicArray has the following parameters:
- int n: the number of empty arrays to initialize in 
- string queries[q]: query strings that contain 3 space-separated integers
"""

def dynamicArray(n, queries):
    dyn_arr = [[] for _ in range(n)]
    last_answer = 0
    answers_arr = []

    for q in queries:
        idx = ((q[1] ^ last_answer) % n)
        if q[0] == 1:
            l = dyn_arr[idx]#.append(q[2])
            l.append(q[2])            
        else:
            last_answer = dyn_arr[idx][q[2] % len(dyn_arr[idx])]
            answers_arr.append(last_answer)
        
    return answers_arr