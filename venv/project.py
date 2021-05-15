# dictionaries
my_dict = {7:"green", 4:"red",5: "blue", 2:"grey"}
print(my_dict[2])
print(my_dict.keys())
print(my_dict.values())

my_dict.update({1 : "white"})
print(my_dict)



# sets
my_set={2,3,4,5,6,7,8,9,9}

my_set2={8,9,0,6,4,3,2}
print(my_set.union(my_set2))
print(my_set.difference(my_set2))
print(my_set.intersection(my_set2))
# #comparison operators
# # if you are write a many programs and these programs are not only to be seen by only you
# # if you wish to have multiple values to be seen by many people
# # flow control
marks = 75
if(marks>80):
    print("Grade A")
elif(marks>60) and (marks <= 60):
    print("Grade B")
elif(marks>40 and marks <=60):
    print("Grade C")
else:
    print("Grade D")
# looping statement when we have two repeated statement
# while loop finding the sum of any number
nums = int(input("Enter the value of n="))
if (nums<= 0):
    print("Enter a valid value")
else:
    sum=0
    while(nums>0):
        sum+=nums
        nums-=1

        print(sum)


# # program
# # for loop
# # creating a program which will keep on decrementing 1
# # executing 99 times,goes down 0,and it has to be decrement 1
# # start point 99
for quantity in range(99,0-1):
    if quantity > 1:
        print(quantity, "bottles of beer on the wall,", quantity ,"bottles of beer")
        if quantity >2:
# u can calculate the value of suffix as a str or as an int
            suf = str(quantity) + "bottle of beer on the wall"
        else:
            suffix = "1 bottle of beer on the wall"
    elif quantity ==1 :
        print("1 bottle of beer on the wall, 1 bottle of beer")
        suffix ="No more beer on the wall"

    print("Take one down and pass it around", suffix)
    print("___")

# break statement
count=0
while True:
    print(count)
    count+=1
    if(count > 10):
        break
# continue
# if the condition has been made then the statement that follows the continue key word it has not to get executed
for y in range(20):
    if(y%2)==0:
        continue
    print(y)
# # functions organised form of instructions or rules that you wish to perform multiple number of times
# # user defined functions and building functions
# #defined user function
def fibo(v):
    a=0
    b=1
    for c in range(y):
        a=b
        b=a+b
        print(a,'\y')
        return b
    num=int(input("Enter the value of y:"))
    print(fibo(v))
# file handling and I/O Methods
# root directory
fp=open("D:\\edureka\\python.txt",'w+')
fp.write("Python is very Good")
fp.write("This was very great")
fp.seek(0)
print(fp.read())
fp.close()

# variables
my_name="mosty"
meaning_of_life=23

print(my_name,meaning_of_life)
# concertinating
full_name=my_name + ' ' + 'Python is good'
print(full_name)

# making a string to lower case
print(my_name.upper(),my_name.lower())

# split strings
firstName="Marina"
lastName="Kyoshabire"
full_name=lastName + firstName
print(full_name.split(' '))

print(full_name.replace('m' ,'f'))
print(lastName.replace('m','f'))

# we can also work with powers and remaiders
x=6
y=3
print('sum',x+y)
print("Difference:",x-y)
print('product:' ,x*y)
print('quotient:' , x/y)
# exponents and remaiders
print('x to the power of y:',x**y)
print('Remaider of x divided by y:',x%y)

 #creating lists
pizza_top=['pineapple','watermellon','pineapple']
print(pizza_top)
# getting the first element
print(pizza_top[1])
# upgrading
pizza_top[1]='mashrooms'
print(pizza_top)
# looking at multiple items
print(pizza_top[0:2])
# one cool little trick
print(pizza_top[::-1])
# practice
stoplight_colors=["green","yellow","broken"]
print(stoplight_colors)
# dictionaries
dict_gloceries={'apple':4,'banana':6,'cookies':5}
print(dict_gloceries.values())
print(dict_gloceries.keys())
# adding a new pair
dict_gloceries['mango']=7
print(dict_gloceries)
# checking a single value
print(dict_gloceries['apple'])

# updating
dict_gloceries['apple']=8
print(dict_gloceries)

# checking for membership
print('apple' in dict_gloceries)
print('watermellon' in dict_gloceries)
#
# backend assesment
#no7

# no 8
l=[]
for h in range( 50):
# for v in l:
    if h % 3 == 0:
        print("Purple")
    elif h % 5 == 0:
        print("White")
    elif h % 3 == 0 & h % 5 == 0:
        print("PurpleWhite")

#no 5
for l in range(10):
    print(l)
# no 6
range(30,50)
for g in range(30,50):
    if g%2!=0:
        print(g)

# no 4
range(1000, 2000)
# s =[]
for c in range:
    if c%7==0 & c % 5 != 0:
        print(c)
# no 1 a/b
a = {6,7,8,9,10}
b ={5,6,7,8,9}
a.add(4)
print(a)
b.add(3)
print(b)

m=a.union(b)
print(m)
print(a.difference(b))
print(a.intersection(b))

# no2
lst= [11, 100, 99, 1000, 999,99]
lst.insert(0,-1)
print(lst)


print(lst[2:3])
print()

# no3
#20021
#2070
years = range(2020, 2070)
for year in years:
    if year%4==0:
        print(year)


