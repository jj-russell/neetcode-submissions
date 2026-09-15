class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        occurrences = {}

        for letter in s:
            if letter not in occurrences:
                occurrences[letter] = 1
            else:
                occurrences[letter] += 1

        for letter in t:
            if letter not in occurrences:
                return False
            elif occurrences[letter] > 1:
                occurrences[letter] -= 1
            else:
                occurrences.pop(letter)

        if occurrences:
            return False
        return True