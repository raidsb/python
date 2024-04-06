"""
You have three stacks of cylinders where each cylinder has the same diameter, but they may vary in height. You can change the height of a stack by removing and discarding its topmost cylinder any number of times.

Find the maximum possible height of the stacks such that all of the stacks are exactly the same height. This means you must remove zero or more cylinders from the top of zero or more of the three stacks until they are all the same height, then return the height.

Example



There are and cylinders in the three stacks, with their heights in the three arrays. Remove the top 2 cylinders from (heights = [1, 2]) and from (heights = [1, 1]) so that the three stacks all are 2 units tall. Return

as the answer.

Note: An empty stack is still a stack.

Function Description

Complete the equalStacks function in the editor below.

equalStacks has the following parameters:

    int h1[n1]: the first array of heights
    int h2[n2]: the second array of heights
    int h3[n3]: the third array of heights

Returns

    int: the height of the stacks when they are equalized

"""

def equalStacks(h1, h2, h3):
    t1 = sum(h1)
    t2 = sum(h2)
    t3 = sum(h3)
    i1 = i2 = i3 = 0 # set to 0 because in the problem statment, the stacks start indexing from the top of the stack on index 0.
    while not (t1 == t2 == t3):
        if t1 > t2 or t1 > t3:
            t1 -= h1[i1]
            i1 += 1
        if t2 > t1 or t2 > t3:
            t2 -= h2[i2]
            i2 += 1
        if t3 > t1 or t3 > t2:
            t3 -= h3[i3]
            i3 += 1
        
    return t1