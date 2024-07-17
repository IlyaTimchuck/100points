import string

content = open('24_medium.txt').read()
all_letters = set(string.ascii_letters.upper())

elements_of_the_number_system = set(string.hexdigits.upper())
forbidden_symbols = all_letters - elements_of_the_number_system
for x in forbidden_symbols:
    content = content.replace(x, ' ')
content = content.split()
d = dict()
for sequences in content:
    if len(sequences) not in d:
        d[len(sequences)] = [len([x for x in sequences if int(x, 16) > 10])]
    else:
        d[len(sequences)].append(len([x for x in sequences if int(x, 16) > 10]))
print(*d[max(d)])
