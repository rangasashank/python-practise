def searcher():
    import time
    # some 4 seconds time consuming task
    namelist = "sashank harry sumit suhas suchi akash rahul akshit vatsav"
    time.sleep(2)

    while True:
        name = (yield)
        if name in namelist:
            print("your name is there in book")
        else:
            print("your name is not there in book")

a = input("Type your name:\n")

search = searcher()
print("searching name ...")
next(search)
search.send(a)

search.close()