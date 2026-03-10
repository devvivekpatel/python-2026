for i in range(1, 5):
    if i == 3:
        continue
    print(i)

total = 0

for i in range(3):
    total += i

print(total)

for i in range(1, 6):
    if i % 2 == 0:
        print(i * 10)
    else:
        print(i)

# for i in range(10, 0, -1):
#     print(i)
# 👉 range(start, stop, step)
# 👉 -1 = backwards
#