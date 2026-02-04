#a

s=input("enter a string:")
s=s.replace("","")
print("frequencies of all character:")

unique_chars=set()
for char in s:
    if char not in unique_chars:
        print(char,":",s.count(char))
        unique_chars.add(char)

#b

s=input("enter a string:")
old=input("enter the character to replace:")
new=input("enter the new character:")
s=s.replace(old,new)
print("updated string:",s)

#c

s=input("enter  string:")
char=input("enter the character to remove:")
index=s.find(char)
if index !=-1:
    s=s[:index]+s[index+1:]
    print("updated string:",s)
else:
    print("character not found.")

#d

s=input("enter a string:")
ch=input("enter the character to remove:")
s=s.replace(ch,"")
print("updated string:",s)



















