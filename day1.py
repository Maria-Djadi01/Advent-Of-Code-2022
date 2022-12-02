f = open('inputs/d1.txt', 'r')
arr = []
sum = 0
i = 0
for line in f:
    # if line is empty then we have new elf records
    if line == '\n':
        arr.append(sum)
        sum = 0
        i += 1
    # if line is not empty then then we sum it up
    else:
        sum += int(line)

########### PART 1 ###########

print(max(arr))

########### PART 2 ###########

top_max = 0

# we pop the first 3 maxes and sum them together
for i in range(3):
    top_max += arr.pop(arr.index(max(arr)))
print(top_max)
