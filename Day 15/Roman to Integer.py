roman = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}


class Solution:
    def romanToInt(self, s: str) -> int:
        return sum(map(lambda part: roman[part] if len(part) == 1 else roman[part[1]] - roman[part[0]], [s[index] if roman[s[min(index + 1, len(s) - 1)]] <= roman[s[index]] else s[index: index + 2] for index in range(len(s)) if roman[s[max(index - 1, 0)]] >= roman[s[index]]]))