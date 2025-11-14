list_a = [4,8,3,7,9]
list_b = [10,3,6,7,2]
list_c = []
i = 0

while i < 5:
    if list_a[i] > list_b[i]:
        list_c.append(list_a[i] - list_b[i] ** 2)
    elif list_a[i] == list_b[i]:
        list_c.append(list_a[i] * 2 % 4)
    else:
        list_c.append((list_b[i] - list_a[i]) // 2)
    i += 1

print(max(list_c))

