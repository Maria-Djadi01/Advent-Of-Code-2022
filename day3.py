f = open('inputs/d3.txt', 'r')
sum1 = 0
half_1 = []
half_2 = []
for line in f:
    half_1 = line[0 : int(len(line) / 2)]
    half_2 = line[int(len(line) / 2) ::]
    for c in half_1:
        if c in half_2:
            if ord(c) >= 65 and ord(c) < 97: sum1 += ord(c) - 38 
            if ord(c) >= 97: sum1 += ord(c) - 96 
            break

print(sum1)

f = open('inputs/d3.txt', 'r')
sum2 = 0

arr_f = []

for line in f:
    arr_f.append(line)

i = 0
while i < len(arr_f):
    for c in arr_f[i]:
        if c in arr_f[i+1] and c in arr_f[i+2]:
            if ord(c) >= 65 and ord(c) < 97: sum2 += ord(c) - 38 
            if ord(c) >= 97: sum2 += ord(c) - 96 
            break
    i += 3
print(sum2)