class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
        	return s

        result = ["" for _ in range(numRows)]
        row, down = 0, 1
        for char in s:
        	result[row] += char

        	if row == numRows - 1:
        		down = 0
        	if row == 0:
        		down = 1

        	if down:
        		row += 1
        	else:
        		row -= 1
        final_string = ""
        for value in result:
        	final_string += value
        return final_string