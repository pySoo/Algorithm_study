def removeDuplicateLetters(self, s):
    stack = []
    # "bcabc" -> suffix: 1) "abc" > a
    # 1) "bcbc" -> suffix: 1-1) "bcbc" > b
    # 1-1) "cc" -> suffix: "cc" > c
    # a+b+c
    for char in sorted(set(s)):
        suffix = s[s.index(char):]
        if set(s) == set(suffix):
            return char + self.removeDuplicateLetters(suffix.replace(char, ''))
    return ''
