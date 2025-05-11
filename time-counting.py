import time
def time_counting(end, start):
    for x in range (start, end, -1):
        print(x)
        time.sleep(1)
    print("Happy new year!!")

time_counting(0 ,10)

