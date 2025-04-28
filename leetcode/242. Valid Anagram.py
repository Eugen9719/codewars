def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    count_s = {}
    count_t = {}
    for char_s, char_t in zip(s, t):
        count_s[char_s] = count_s.get(char_s) + 1 if char_s in count_s else 1
        count_t[char_t] = count_s.get(char_t) + 1 if char_t in count_t else 1

    return count_s == count_t


print(isAnagram("anagram", "nagaram"))
print(isAnagram("rat", "car"))
