class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        # 1. Build the target map for s1
        target = {}
        for char in s1:
            target[char] = target.get(char, 0) + 1

        # 2. Build the initial window map for the first len(s1) characters of s2
        window = {}
        for i in range(n1):
            char = s2[i]
            window[char] = window.get(char, 0) + 1

        # 3. Check the first window
        if window == target:
            return True

        # 4. Slide the window across s2
        for i in range(n1, n2):
            # Character entering the window (right side)
            right_char = s2[i]
            window[right_char] = window.get(right_char, 0) + 1
            
            # Character leaving the window (left side)
            left_char = s2[i - n1]
            if window[left_char] == 1:
                del window[left_char]  # Remove key so dictionary comparison works
            else:
                window[left_char] -= 1
            
            # Compare maps
            if window == target:
                return True
                
        return False