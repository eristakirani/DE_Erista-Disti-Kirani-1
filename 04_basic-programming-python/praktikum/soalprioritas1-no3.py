for i in range(1, 101):
    if i%3==0 and i%5==0:
        print("buzz")
    elif i%5==0: 
        print(i*i*i)
    elif i%3==0:
        print(i*i)
    else:
        print(i)