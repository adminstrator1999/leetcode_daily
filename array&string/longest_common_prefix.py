from typing import List


class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''

        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res

    def longestCommonPrefixTrie(self, strs: List[str]) -> str:
        # trie data structure
        trie = {}
        for word in strs:
            cur = trie
            for letter in word:
                if letter not in cur:
                    cur[letter] = {}
                cur = cur[letter]
            cur['#'] = {}
        res = ''

        while len(trie) == 1:
            key = list(trie.keys())[0]
            if key == "#":
                break
            res += key
            trie = trie[key]
        return res

strs = [ "flower", "flow", "flight"]
# strs = ["dog", "racecar", "car"]
# strs = ["a"]
solution = Solution()
print(solution.longestCommonPrefix(strs))
