l=[]
for i in range(3):
    n=int(input("Enter the no.:"))
    l.append(n)
big=0
for i in l:
    if i>big:
        big=i;
print("The Biggest no. of all 3 is:",big)