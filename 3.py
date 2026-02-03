def even_odd(num):
    if num%2==0:
        return True
    else:
        return False
num=int(input("enter a number:"))
if even_odd(num):
    print(num,"is even")
else:
    print(num,"is odd") 
