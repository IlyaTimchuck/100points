content = open('24_light.txt').read().split()
columns = []
for x in range(len(content)):
    st = ''
    for y in range(len(content)):
        st += content[y][x]
    columns.extend(st.split('0'))
print(max(len(x) for x in columns))
