class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1  # 2147483647
        INT_MIN = -2**31     # -2147483648
        
        sign = -1 if x < 0 else 1
        x = abs(x)
        reversed_num = 0
        
        while x != 0:
            digit = x % 10
            x //= 10
            
            # Check for overflow before updating reversed_num
            if reversed_num > INT_MAX // 10:
                return 0
            
            # If reversed_num == INT_MAX // 10, check the last digit
            if reversed_num == INT_MAX // 10:
                if sign == 1 and digit > 7:  # 2147483647 % 10 = 7
                    return 0
                if sign == -1 and digit > 8:  # 2147483648 % 10 = 8
                    return 0
                    
            reversed_num = reversed_num * 10 + digit
        
        return sign * reversed_num
        