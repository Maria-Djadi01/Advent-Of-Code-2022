########### PART 1 ###########

f = open('inputs/d4.txt', 'r')

sum1 = 0
paire = []
for line in f:
    paire.append(line.split(','))

for p in paire:
    p1 = p[0].split('-')
    p2 = p[1].split('-')
    
    if int(p1[0]) <= int(p2[0]) and int(p1[1]) >= int(p2[1]): sum1 += 1
    elif int(p2[0]) <= int(p1[0]) and int(p2[1]) >= int(p1[1]): sum1 += 1
print(sum1)

########### PART 2 ###########
sum2 = 0
for p in paire:
    p1 = p[0].split('-')
    p2 = p[1].split('-')
    
    if int(p1[0]) <= int(p2[0]) and int(p1[1]) >= int(p2[0]): sum2 += 1
    elif int(p1[0]) <= int(p2[1]) and int(p1[1]) >= int(p2[1]): sum2 += 1
    elif int(p2[0]) <= int(p1[0]) and int(p2[1]) >= int(p1[0]): sum2 += 1
    elif int(p2[0]) <= int(p1[1]) and int(p2[1]) >= int(p1[1]): sum2 += 1
print(sum2)







