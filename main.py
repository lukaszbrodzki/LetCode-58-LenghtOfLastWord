class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(" ")[-1])


if __name__ == '__main__':
   s = Solution()
   test = "   fly me   to   the moon  "
   print(s.lengthOfLastWord(test))
