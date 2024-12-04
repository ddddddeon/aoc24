from util import load_columns

def contains(l, n):
    occurrences = 0
    for item in l:
        if int(item) == n:
            occurrences += 1
    return occurrences


l1, l2 = load_columns("./input.txt")    

similarity_score = 0
for num in l1:
    num = int(num)
    similarity_score += num * contains(l2, num)

print(similarity_score)
    
