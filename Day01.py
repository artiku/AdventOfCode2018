with open("day01input.txt") as f:
    content = f.readlines()

content = [x.strip() for x in content]

freq = 0
for row in content:
    num = int(row[1:])
    if row[0] == '+':
        freq += num
    else:
        freq -= num

print(freq)

# second star

freq = 0
lst = [0]
flag = False
while not flag:
    for row in content:
        num = int(row[1:])
        if row[0] == '+':
            freq += num
        else:
            freq -= num
        lst.append(freq)
        if len(set(lst)) != len(lst):
            print(freq)
            flag = True
            break

