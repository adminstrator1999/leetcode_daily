from typing import List
from collections import Counter

class Solution:

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        for c in ransomNote:
            if ransomNote.count(c) > magazine.count(c):
                return False
        return True

    def canConstructEasy(self, ransomNote: str, magazine: str) -> bool:
        note_counter = Counter(ransomNote)
        letter_pool = Counter(magazine)
        for key, value in note_counter.items():
            if key not in letter_pool or letter_pool[key] < value:
                return False
        return True


ransomNote = "a"
magazine = "b"
solution = Solution()
print(solution.canConstruct(ransomNote, magazine))
