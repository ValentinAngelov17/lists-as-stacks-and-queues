from collections import deque
s = deque()


while True:
    name = input()
    if name == "Paid":
        while s:
            paid = s.popleft()
            print(paid)
    elif name == "End":
        print(f"{len(s)} people remaining.")
        break
    else:
        s.append(name)
