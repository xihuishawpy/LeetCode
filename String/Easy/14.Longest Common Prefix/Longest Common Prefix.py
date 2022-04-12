#方法一，利用zip，更快
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        return (
            next(
                (
                    strs[0][:i]
                    for i, letter_group in enumerate(zip(*strs))
                    if len(set(letter_group)) > 1
                ),
                min(strs),
            )
            if strs
            else ""
        )
        
#方法二，利用reduce  
class Solution:

    def lcp(self, str1, str2):
        i = 0
        while (i < len(str1) and i < len(str2)):
            if str1[i] == str2[i]:
                i += 1
            else:
                break
        return str1[:i]
                                                                                                                                            
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        return reduce(self.lcp,strs) if strs else ''