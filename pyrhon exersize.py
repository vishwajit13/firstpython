''''birth_year=int(input("enter ur birth year :"))
current_year=int(input("enter current year:"))
age=(current_year -  birth_year)
print('your age is:',age)

 f_name=input("enter your first name= ")
m_name=input("enter your middle name= ")
l_name=input("enter your last name= ")
name=f_name+m_name+l_name
print("your name is",name)


f_long=92
f_width=48.8
area=f_long * f_width
print("total area of that foootboll ground is;",area)


potato_chips=9
one_packet=1.49
given_aaamo=20
shop_ammo=9*1.49
ammo_return=given_aaamo-shop_ammo
print("returned ammont is",ammo_return)


lenghth_bath_sf=5.5**2
per_suare_feet=500
total_cost=lenghth_bath_sf*per_suare_feet
print("total coast to replace all styles",total_cost)

num=17
print("number in binary",format(num,'b'))


street=input("enter the name of street ")
city=input("enter the name of city")
country=input("enter the name of country")
print("your address:",street+'\n'
      +city+'\n'+
      country+'\n')


s='earth revolves around the sun'

print(s[

vegitables=input(" vegitable names that you eat daily")
fruits=input("fruits names that you eat daily")
print(f" i eat {vegitables} vegitables and {fruits} fruits daily")


s='maine 200 banana khaye'
s=s.replace('banana','samosa').replace('200','10')
print(s
)

exp=[2200,2350,2600,2130,2190]
print("extra dollers compare to january in feb",exp[0]-exp[1])

print("total income in first quarter",exp[1]+exp[2]+exp[0])
print("did ispened 2000 in any of the month",2000 in exp)


exp.append(1980)
print("expence when jun is complited",exp)
exp[3]=exp[3]-200
print("the month after reducing200 from it",exp[3])
print(exp)



india=["mumbai","bangalore","chennai","delhi"]
pakistan=["lahore","karachi","islamabad"]
bangladesh=["dhaka","khulna","rangpur"]

city1=input("enter the city name1")
city2=input("enter the city name2")


if city1 in india and city2 in india:
    print(f"the both belongs to india")

elif city1 and city2 in pakistan:
    print(f"the  both belongs to pakistan")
elif city1 and city2 in bangladesh:
    print(f"the both belongs to bangladesh")
else:
    print("they are not belongs to one country")



shugar_level=input("enter the sugar level")
shugar_level=int(shugar_level)
if shugar_level<100:
    print("shugar is low")
elif shugar_level>100:
    print("shugar is high")
else:
    print("sugar is norml")


result=["heads","tails","tails","heads","tails","heads","heads","tails","tails"]
count=0

for i in result:
    if i=="tails":
        count+=1
        print("head count is",count)




num=[1,3,5,7,9]
i=0
for i in num:

    print('sqaure of  num are',i*i)

    for i in range (1,11):
        if i%2==0:
          continue
        print(i*i)

for i in range(1,6):
    s=''
    for j in range(i):
        s+='*'
        print(s)

base=input("enter the base value")
height=input("enter the height value")
base=int(base)
height=int(height)
area=1/2*base*height
area=int(area)
print(area)'''


f=open("c:\\python\\poem.txt","r")
print(f.read())
f.close()