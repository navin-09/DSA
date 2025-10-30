def generator(n):
    for i in range(n):
        yield i*i

for x in generator(5):
    print(x)
