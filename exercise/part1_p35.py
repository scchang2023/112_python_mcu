a=int(input("a="))
b=int(input("b="))
print(f"a={a},b={b}")

c=a
a=b
b=c
print(f"a={a},b={b}")

a=a+b
b=a-b
a=a-b
print(f"a={a},b={b}")

a,b=b,a
print(f"a={a},b={b}")