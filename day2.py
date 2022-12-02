# X : 1
# Y : 2
# Z : 3

# WIN : 3
# LOSE : 0


########### PART 1 ###########
f = open('inputs/d2.txt', 'r')
score1 = 0

for line in f:
    match line[2]:
        case 'X':
            score1 += 1
            match line[0]:
                case 'A': score1 += 3
                case 'B': score1 += 0
                case 'C': score1 += 6
    match line[2]:
        case 'Y':
            score1 += 2
            match line[0]:
                case 'A': score1 += 6
                case 'B': score1 += 3
                case 'C': score1 += 0
    match line[2]:
        case 'Z':
            score1 += 3
            match line[0]:
                case 'A': score1 += 0
                case 'B': score1 += 6
                case 'C': score1 += 3

print(score1)

########### PART 2 ###########
score2 = 0
f = open('inputs/d2.txt', 'r')

for line in f:
    match line[2]:
        case 'X':
            match line[0]:
                case 'A': score2 += 3
                case 'B': score2 += 1
                case 'C': score2 += 2
    match line[2]:
        case 'Y':
            score2 += 3
            match line[0]:
                case 'A': score2 += 1
                case 'B': score2 += 2
                case 'C': score2 += 3
    match line[2]:
        case 'Z':
            score2 += 6
            match line[0]:
                case 'A': score2 += 2
                case 'B': score2 += 3
                case 'C': score2 += 1
print(score2)