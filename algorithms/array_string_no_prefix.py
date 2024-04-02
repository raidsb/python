"""
There is a given list of strings where each string contains only lowercase letters from

, inclusive. The set of strings is said to be a GOOD SET if no string is a prefix of another string. In this case, print GOOD SET. Otherwise, print BAD SET on the first line followed by the string being checked.

Note If two strings are identical, they are prefixes of each other.

Example

Here 'abcd' is a prefix of 'abcde' and 'bcd' is a prefix of 'bcde'. Since 'abcde' is tested first, print

BAD SET  
abcde

.

No string is a prefix of another so print

GOOD SET 

Function Description
Complete the noPrefix function in the editor below.

noPrefix has the following parameter(s):
- string words[n]: an array of strings 

https://www.hackerrank.com/challenges/one-month-preparation-kit-no-prefix-set/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-four 
"""


def noPrefix(words):
    c1, c2 = set(), set()
    for word in words:
        # word 'b' is a prefix in the previous words like ['bacd', .. :
        if word in c2:
                print(f"BAD SET\n{word}")
                return
        
        # prefix 'b' from word 'bacd' is in the previous words like ['b', .. :
        for prefix in (word[:i] for i in range(1,len(word)+1)):
            if prefix in c1:
                print(f"BAD SET\n{word}")
                return
            c2.add(prefix)
        c1.add(word)
        
    print("GOOD SET")