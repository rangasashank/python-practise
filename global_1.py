l = 10 #global
def f1(n):
    l = 5 #local
    m = 8 #local
    global l 
    l = l+45
    print(l, m)
    print(n, "I printed")

f1("this is me")
print(l)