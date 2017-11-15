class Solution:
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        letters = [False] * 26
        for char in s:
            if ord(char) - ord('a') < 26:
            	letters[ord(char) - ord('a')] = True

        result = ""
        for bool_index in range(len(letters)):
        	if letters[bool_index]:
        		result = result + chr(ord('a') + bool_index)

        return result

case = Solution()
print(case.removeDuplicateLetters("alkdfjalsgjabacaae") == "abcdefgjkls")
print(case.removeDuplicateLetters("") == "")
