for i in range(1, 101):
    if i % 7 == 0 or "7" in str(i):
        continue
    print(i)
    # id i % x_boom !=0 and not str(x_boom) in str(i)
else:
    print("loop finished successfully")
