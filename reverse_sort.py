from random import randint
def reverse_sort(*args):
    c = []
    for t in args:
        c.append(t)
    c = sorted(c, key=lambda x: abs(c.index(x)-len(c)))
    return c

def product_odd(*args):
    t = []
    w = []
    q = []
    for x in args:
        for y in args:
            if x != y:
                t.append((x, y))
    for (l, m) in t:
        if (m, l) not in q:
            q.append((l, m))
        else:
            pass
    for k, z in q:
        if (k * z) % 2 != 0:
            w.append((k, z))
    return w

def my_shuffle(data):
    new_list = []
    indices = []
    for x in range(0, len(data)):
        new_list.append(0)
    while len(indices) != len(data):
        c = randint(0, len(data)-1)
        if c not in indices:
            indices.append(c)
        else:
            continue
    for y in indices:
        new_list[y] = data[indices.index(y)]
    return new_list


x = [i for i in range(1, 6)]

t = []

for y in range(0, len(x)):
    t.append(my_shuffle(x))

print(t)

print(t[2][3])

for z in t:
    print(z)