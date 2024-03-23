def countingSort(arr):
    counting_l = [0] * 100
    for i in arr:
        counting_l[i] += 1
    
    return counting_l
