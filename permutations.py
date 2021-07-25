from math import factorial
data_x = list('catdog')

array = []

def permutations(data, x, y):
    if x == y:
        print("".join(data))
        array.append("".join(data))
    else:
        for i in range(x, y):
            data[x], data[i] = data[i], data[x]
            permutations(data, x+1, y)
            data[i], data[x] = data[x], data[i]

permutations(data_x, 0, len(data_x))

i = 0

with open("list_of_permutations.txt", mode="w") as contents:
    for x in array:
        contents.write("%s\n" % x)

    
