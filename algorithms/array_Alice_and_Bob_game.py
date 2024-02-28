"""
The question about Alice and Bob game
"""

class Solution(object): 

    def divisorGame(self, n): 

        """ 

        :type n: int 

        :rtype: bool 

         

        alice start first  

        choose x where 0 < x < n  

        choose x where n % x == 0 

        when chosen change the number on board to n - x 

        """ 

         

        current_player = "alice" 

        x = n - 1 

        print("x = ", x) 

        while x > 0:                         

            print("n % x = ", n % x) 

            if n % x == 0: 

                # found a number to play with 

                n = n - x 

                x = n - 1 

                if x > 0:  

                    current_player = "bob" if current_player == "alice" else "alice" 

            else:  

                x = x - 1 

             

                 

        if current_player == "alice": 

            return True 

        else:  

            return False 
