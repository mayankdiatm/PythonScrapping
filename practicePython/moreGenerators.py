#Alpha generators
def alphaGen(start, end):
    for i in range(ord(start), ord(end) + 1):
        yield chr(i)


res = alphaGen("a", "g")
for char in res:
    print(char)

    # cList = list(res)
    # print(cList)