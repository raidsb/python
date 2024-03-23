"""
Julius Caesar protected his confidential information by encrypting it using a cipher. Caesar's cipher shifts each letter by a number of letters. If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet. In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.

Original alphabet:      abcdefghijklmnopqrstuvwxyz
Alphabet rotated +3:    defghijklmnopqrstuvwxyzabc
Example


The alphabet is rotated by , matching the mapping above. The encrypted string is .

Note: The cipher only encrypts letters; symbols, such as -, remain unencrypted.

Function Description

Complete the caesarCipher function in the editor below.

caesarCipher has the following parameter(s):

string s: cleartext
int k: the alphabet rotation factor
Returns

string: the encrypted string

"""
def caesarCipher(s, k):
    new_string = ''
    for c in s:
        if c.isalpha():
            if (c.islower()):
                new_string += chr((ord(c) - ord('a') + k) % 26 + ord('a'))
            else:
                new_string += chr((ord(c) - ord('A') + k) % 26 + ord('A'))
        else:
            new_string += c
    
    return new_string