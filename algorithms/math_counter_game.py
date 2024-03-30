"""
In the Counter Game problem on HackerRank, the solution involves a game where players alternately remove tokens from a pile until the pile becomes empty. The game follows certain rules, such as each player can only remove a power of 2 number of tokens at each turn.

The use of counting set bits (bits set to 1) in this problem might relate to determining the winner of the game efficiently. Specifically, when a player removes tokens from the pile, the number of tokens left becomes a power of 2 after each turn. This is because the player can only remove a power of 2 number of tokens, and thus, the number of tokens left will always have a binary representation with only one bit set to 1.

By counting the number of set bits in the binary representation of the current number of tokens, the players can determine whether the current number is a power of 2. If the number of set bits is exactly 1, then the number is a power of 2, indicating that it's the losing state for the current player. Conversely, if the number of set bits is greater than 1, the player can make a move that results in the opponent encountering a losing state.

This strategy allows players to efficiently play the game and make optimal moves based on the number of tokens remaining in the pile. It's a clever use of bitwise operations and counting set bits to determine the winning strategy in the Counter Game problem.


Louise and Richard have developed a numbers game. They pick a number and check to see if it is a power of . If it is, they divide it by . If not, they reduce it by the next lower number which is a power of . Whoever reduces the number to  wins the game. Louise always starts.

Given an initial value, determine who wins the game.

Example

It's Louise's turn first. She determines that  is not a power of . The next lower power of  is , so she subtracts that from  and passes  to Richard.  is a power of , so Richard divides it by  and passes  to Louise. Likewise,  is a power so she divides it by  and reaches . She wins the game.

Update If they initially set counter to , Richard wins. Louise cannot make a move so she loses.

Function Description

Complete the counterGame function in the editor below.

counterGame has the following parameter(s):

int n: the initial game counter value
Returns

string: either Richard or Louise

"""


working one from discussion 
def counterGame(n):
    count = 0
    while(n > 1):
        if int(bin(n)[3:]) == 0: # starting from the fourth character, in python the first two is used to represent the bin "0b" and the the bit in index 3 is also ignored because can be 1 is ok. we care about the bits after
            n //= 2
        else:
            power_of_2 = 1 << len(bin(n)[3:])
            n -= power_of_2
        count += 1
    return 'Richard' if count % 2 == 0 else 'Louise'

explanation on line 39 why using this condition 
Certainly! Let's break down the explanation with an example:

Suppose we have n = 40. The binary representation of n is '0b101000'.

bin(40) returns '0b101000'
We're interested in checking if the binary representation starting from the third character (after ignoring the prefix '0b') is all zeros.
So, bin(40)[3:] returns '101000'. This represents the binary digits of n without the prefix.

Now, the condition int(bin(n)[3:]) == 0 checks if this binary representation ('101000') is equal to zero when converted back to an integer. If it's equal to zero, it means that the binary representation contains only zeros after the initial '1'. In our example, '101000' is not equal to zero, so the condition is false.

Here's another example:

Suppose we have n = 16. The binary representation of n is '0b10000'.

bin(16) returns '0b10000'
bin(16)[3:] returns '10000'
The condition int(bin(16)[3:]) == 0 checks if '10000' (the binary representation of 16 without the prefix) is equal to zero when converted back to an integer. In this case, '10000' is equal to zero, so the condition is true.


below from chatgpt didn't work
def count_set_bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

def counter_game(N):
    # Count the number of set bits in N
    set_bits_count = count_set_bits(N)
    
    # If the count of set bits is odd, Player 1 wins; otherwise, Player 2 wins
    if set_bits_count % 2 == 1:
        return "Louise"
    else:
        return "Richard"
		
		