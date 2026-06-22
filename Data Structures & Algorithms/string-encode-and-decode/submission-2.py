from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        # O(N) time - Joins strings with the pattern: €[length]π[string]
        return "".join(f"€{len(s)}π{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0
        
        # O(N) time - Single pass pointer architecture
        while i < len(s):
            if s[i] == "€":
                # Find the 'π' delimiter starting from the current '€'
                pi_index = s.find("π", i)
                
                # Extract and parse the length integer
                length = int(s[i + 1:pi_index])
                
                # Slice the exact string using the parsed length
                start_str = pi_index + 1
                end_str = start_str + length
                decoded_strs.append(s[start_str:end_str])
                
                # JUMP the pointer past the processed string
                i = end_str
            else:
                i += 1
                
        return decoded_strs
