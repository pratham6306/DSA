class Solution(object):
    def sequentialDigits(self, low, high):
        sample = "123456789"
        result = []
        
        # Calculate lengths of the minimum and maximum possible numbers
        min_len = len(str(low))
        max_len = len(str(high))
        
        # Slide a window of length 'length' across the sample string
        for length in range(min_len, max_len + 1):
            for start in range(10 - length):
                num = int(sample[start:start + length])
                
                # Check if the generated number falls within the requested range
                if low <= num <= high:
                    result.append(num)
                    
        return result
