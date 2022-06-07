# Given a string s, return the longest palindromic substring in s.

def fn(s):
    longest = s[0]
    for i in range(1, len(s)):
        l = r = i
        while (l >= 0 and r < len(s)):
            if s[l] != s[r]:
                break
            longest = s[l:r+1] if len(s[l:r+1]) > len(longest) else longest
            l -= 1
            r += 1

        r, l = i-1, i
        while (l >= 0 and r < len(s)):
            if s[l] != s[r]:
                break
            longest = s[l:r+1] if len(s[l:r+1]) > len(longest) else longest
            l -= 1
            r += 1

    return longest


out = fn("heleh")
print(out)