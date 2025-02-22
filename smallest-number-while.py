# n = float(input("n: "))
# min = n
# while True :
#     s =input("Do you continue?")
#     if s.lower()=="no" :
#         break
#     n = float(input("n: "))
#     if n < min :
#         min =n
# print(min, "is esmallest number")


min = float("inf")
while True :
    n = float(input("n: "))
    if n < min :
        min =n
    s =input("Do you continue?")
    if s.lower()=="no" :
        break
    
print(min, "is esmallest number")
