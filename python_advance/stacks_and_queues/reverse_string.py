text = input()

s = []
for c in text:
    s.append(c)

reverse_string = ''

while s:
    reverse_string += s.pop()
