def solution(s):
    palindromes = {}

    def isPalindrome(s):
        if palindromes.get(s) is not None:
            return palindromes[s]

        l = len(s) // 2 - 1 if len(s) % 2 == 0 else len(s) // 2
        r = len(s) // 2

        while l >= 0:
            if s[l] != s[r]:
                palindromes[s] = False
                return False
            l -= 1
            r += 1

        while l >= 0:
            if s[l] != s[r]:
                palindromes[s] = False
                return False
            l -= 1
            r += 1

        palindromes[s] = True
        return True

    visited = set()

    def recurse(s, i, j):
        if (i, j) in visited:
            return 0

        if i == j:
            return 0

        visited.add((i, j))

        return recurse(s, i+1, j) + recurse(s, i, j-1) + isPalindrome(s[i:j])

    return recurse(s, 0, len(s))

a = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
out = solution(a)
print(out)



    # def countSubstrings(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
        
    #     ans = 0
    #     mid = 0
    #     n = len(s)
    #     while mid < n:
    #         left = mid - 1
    #         right = mid
            
    #         while right < n - 1 and s[right] == s[right+1]: 
    #             right += 1
    #         ans += (right - left) * (right - left + 1) // 2
    #         mid = right + 1
    #         right = right + 1
            
    #         while left >= 0 and right < n and s[left] == s[right]:
    #             left -= 1
    #             right += 1
    #             ans += 1
                
    #     return ans
            
