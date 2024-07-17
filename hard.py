import string

content = open('24_hard.txt').read()


def sum_of_digits(s):
    return sum(int(s[i]) for i in range(0, len(s), 2))


mx = 0
sequence = ''
num = string.digits
all_letters = string.ascii_letters

for i in range(1, len(content)):
    char1 = content[i - 1]
    char2 = content[i]

    if (char1 in num and char2 in all_letters) or (char1 in all_letters and char2 in num):
        sequence += char2
        if sequence[0] in num and sum_of_digits(sequence) == len(sequence):
            mx = max(mx, len(sequence))
    else:
        sequence = ''

print(mx)
