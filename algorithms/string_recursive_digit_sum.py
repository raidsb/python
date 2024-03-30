"""
We define super digit of an integer  using the following rules:

Given an integer, we need to find the super digit of the integer.

If  has only  digit, then its super digit is .
Otherwise, the super digit of  is equal to the super digit of the sum of the digits of .
For example, the super digit of  will be calculated as:

	super_digit(9875)   	9+8+7+5 = 29 
	super_digit(29) 	2 + 9 = 11
	super_digit(11)		1 + 1 = 2
	super_digit(2)		= 2  
Example


The number  is created by concatenating the string   times so the initial .

    superDigit(p) = superDigit(9875987598759875)
                  9+8+7+5+9+8+7+5+9+8+7+5+9+8+7+5 = 116
    superDigit(p) = superDigit(116)
                  1+1+6 = 8
    superDigit(p) = supe
"""

def superDigit(n, k):
    if k == 1:
        if len(n) == 1:
            return int(n)
        else:
            sum_of_digit = sum(map(int, n))
            return superDigit(str(sum_of_digit), 1)
    else:
        sum_of_digit = sum(map(int, n))
        new_n = [str(sum_of_digit)] * k
        return superDigit(new_n, 1)