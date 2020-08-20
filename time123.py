import time
initial = time.time()

k = 0
while(k<20):
    print("sashi")
    k += 1
print(f"while loop ran in {time.time() - initial} seconds")

initial2 = time.time()
for i in range(20):
    print("sashi")
print(f"for loop ran in {time.time() - initial2} seconds")
