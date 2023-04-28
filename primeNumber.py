n = int(input("Enter the number that has to be checked: "))
a = 0
for i in range(2, int(n / 2)):
    if n % i == 0:
        # finding whether the number has a factor or not
        a = a + 1
if a > 0:
    print("The number is not prime")
else:
    print("The number is prime")
