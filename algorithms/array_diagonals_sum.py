 

def diagonalDifference(arr): 

    diag1_sum = 0 

    diag2_sum = 0 

    for i in range(0, len(arr)): 

        diag1_j = i 

        diag2_j = len(arr) - 1 - i 

        diag1_sum += arr[i][diag1_j] 

        diag2_sum += arr[i][diag2_j] 

 
 

    return abs(diag1_sum - diag2_sum) 
