class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        Calculate the Hamming weight (number of '1' bits) in the binary representation of n.
      
        Uses Brian Kernighan's algorithm: n & (n-1) clears the least significant set bit.
        Each iteration removes one '1' bit until n becomes 0.
      
        Args:
            n: A positive integer
          
        Returns:
            The number of '1' bits in the binary representation of n
        """
        # Initialize counter for number of 1 bits
        count = 0
      
        # Continue while there are still 1 bits remaining
        while n:
            # Clear the least significant set bit
            # Example: n = 1100, n-1 = 1011, n & (n-1) = 1000
            n &= n - 1
          
            # Increment the count as we've removed one 1 bit
            count += 1
      
        return count
