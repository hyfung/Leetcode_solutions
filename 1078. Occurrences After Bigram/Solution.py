class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        # Tokenize strings
        text = text.split(' ')
        res = []
        
        # Sliding window
        for i in range(len(text) - 2):
            if text[i] == first and text[i+1] == second:
                res.append(text[i+2])
        
        return res
