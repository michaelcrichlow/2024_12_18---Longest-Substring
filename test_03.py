def sumDigits(n: int) -> int:
    _n = n
    total = 0
    div, mod = 1_000, 0

    while div > 0:
        div, mod = divmod(_n, 10)
        total += mod
        _n = div

    return total


def sumOfDigits(l: list[int]) -> int:
    total = 0
    for val in l:
        total += sumDigits(val)

    return total


def isAlphabet(s: str) -> bool:
    return s.isalpha()


def findShortestWord(s: str) -> str:
    _s = s.split()
    res = _s[0]
    for val in _s:
        if len(val) < len(res):
            res = val

    return res


def sumEvenNumbers(l: list[int]) -> int:
    total = 0
    for val in l:
        if val % 2 == 0:
            total += val

    return total


def longestSubstring(s: str) -> int:
    local_dict = dict()
    length = 0
    max_length = 0
    for i in range(len(s)):
        length = 1
        local_dict[s[i]] = 0
        for j in range(len(s)):
            if j > i:
                if s[j] not in local_dict:
                    local_dict[s[j]] = 0
                    length += 1
                    if max_length < length:
                        max_length = length
                else:
                    local_dict.clear()
                    length = 0
                    break

    return max_length


def main() -> None:
    # print(sumOfDigits([12, 34, 56]))
    # print(isAlphabet("helloWorld"))
    # print(findShortestWord("I have a cat."))
    # print(sumEvenNumbers([1, 2, 3, 4, 5, 6]))
    print(longestSubstring("abcabcbb"))


if __name__ == '__main__':
    main()

# sumDigits(123) => 6
# sumOfDigits([12, 34, 56]) should return 21
# isAlphabet('helloWorld') => true
# findShortestWord('I have a cat.') => 'I'
# sumEvenNumbers([1, 2, 3, 4, 5, 6]) => 12
# longestSubstring('abcabcbb') => 3
