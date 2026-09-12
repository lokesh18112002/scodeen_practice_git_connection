

def fuxn(*n):
    t=sum(n)
    return t


print(fuxn(5,5,5,5))

def sub(*n):
    sub = n[0]
    for num in n[1:]:
        sub-=num
    return sub

print(sub(20,5,5))