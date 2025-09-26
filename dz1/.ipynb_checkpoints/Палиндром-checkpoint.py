# Номер3
count = 0
a = str(input())


def palindrom(a):
    for i in range(0, (len(a)) // 2):
        j = len(a) - i - 1
        if a[i] == a[j]:
            count += 1


if count == len(a) // 2:
    return ("is a regular palindrome.")


def mirror(a):
    mirror_dict = {'A': 'A', 'H': 'H', 'I': 'I', 'M': 'M', 'O': 'O',
                   'T': 'T', 'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X',
                   'Y': 'Y', '1': '1', '8': '8',
                   'E': '3', '3': 'E',
                   'J': 'L', 'L': 'J',
                   'S': '2', '2': 'S',
                   'Z': '5', '5': 'Z'}


mirror_chars = []
for char in a:
    if char in mirror_dict:
        mirror_chars.append(mirror_dict[char])
    else:
        return False

mirror_str = ''.join(mirror_chars)
return mirror_str == s[::-1]


def check(a):
    palindrome_check = palindrom(a)
    mirror_check = mirror(a)

    if palindrome_check and mirrored_check:
        return f"{a} is a mirrored palindrome."
    elif palindrome_check:
        return f"{a} is a regular palindrome."
    elif mirrored_check:
        return f"{a} is a mirrored string."
    else:
        return f"{a} is not a palindrome."


'''

'''
# Номер4
nums = list(map(int, input().split()))
for i in range(0, 2 * len(nums) // 2 - 1, 2):
    nums[i], nums[i + 1] = nums[i + 1], nums[i]
print(nums)