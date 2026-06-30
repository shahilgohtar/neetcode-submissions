class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = n 
        
        while True:
            slow = self.square_sum(slow)
            fast = self.square_sum(self.square_sum(fast))

            if slow == fast:
                return slow == 1
        
    def square_sum(self,n):
        total  = 0

        while n > 0:
            digit = n % 10
            total += digit * digit
            n //= 10
        return total

        


        