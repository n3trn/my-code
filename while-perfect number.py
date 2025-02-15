a =1
r = []
x = int (input("satr: "))
while a <= x :
    if x%a==0:
        r.append(a)
    a+=1
if sum(r)-x==x :
    print("complete")
else:
    print("nis")