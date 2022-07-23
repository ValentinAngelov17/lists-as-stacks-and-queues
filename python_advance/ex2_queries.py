stack = []

queries_Count = int(input())

for _ in range(queries_Count):
    queries_parts = [int(x) for x in input().split()]
    command = queries_parts[0]

    if command == 1:
        number = queries_parts[1]
        stack.append(number)
    elif command == 2 and stack:
        stack.pop()
    elif command == 3 and stack:
        print(max(stack))
    elif command == 4 and stack:
        print(min(stack))

reversed_stack = []
while stack:
    reversed_stack.append(str(stack.pop()))

print(", ".join(reversed_stack))
