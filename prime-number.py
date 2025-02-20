n = int (input("n: ")) #3
i = 2
if n > 1 :
    while i < n :
        if n % i == 0 :
            print(n , "not prime")
            break
        i+=1
    else:
        print(n,'prime')
else:
    print(n,'not prime')