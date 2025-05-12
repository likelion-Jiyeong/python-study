# execute time shorter version
# class Solution:
#     def longeastCommonPrefix(self, strs):
#         if not strs:
#             return ""
        
#         prefix = strs[0]

#         for i in strs[1:]:
#             while not i.startswith(prefix):
#                 prefix = prefix[:-1]
#                 if prefix == "":
#                     return ""
        
#         return prefix
    

# solution = Solution()
# strs = ["flower","flow","flight"]
# answer = solution.longeastCommonPrefix(strs)
# print(f"answer >> {answer}")

# original my code
class Solution:
    def longeastCommonPrefix(self, strs):
        strs.sort(key=lambda x: len(x))
        
        if len(strs) == 0:
            return ""
        else:
            for i in range(len(strs[0])):
                for j in range(1, len(strs)):
                    if strs[0][i] != strs[j][i]:
                        return strs[0][:i]
            return strs[0]

solution = Solution()
strs = ["flower","flow","flight"]
answer = solution.longeastCommonPrefix(strs)
print(f"answer >> {answer}")
