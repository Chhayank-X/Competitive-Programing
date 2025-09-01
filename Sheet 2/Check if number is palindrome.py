A = int(input())
x = A
rev = 0
while A > 0:
    rev = rev * 10 + A % 10
    A //= 10
if x == rev:
    print("Yes")
else:
    print("No")
