L1=[1,2,3,4,5,"Ahmed"]
print(type(L1))
a=list()                   #لازم اكتب كلمة list
print(a)
b=list("abcdefg")           #لازم اكتب كلمة list 
print(type(b))
#Range
c=list(range(100))
d=[0]*5
print(c)
print(d)
#creating lists from string and Ranges
           #1
my_string="I am learning pyhon"
my_new_list=list(my_string)
print(my_new_list)
             #2
my_range_list=list(range(200))     
print(my_range_list)         
# lists indexing : the fisrt items at index is [0] and he second item is[1] .....so on
l1 = [2,6,9,"rehab"] # بعؤف اقدر اجيب الايتم م مرتبته في اللسته
print(l1[0])
print(l1[-1]) 
# list slicing
# list[start:stop]
L1=[1,2,3,4,5,100]
print(L1[1:4])
# list[start:stop:stop]
print(L1[0:2:3])
print(L1[::-1]) # بالعكس
print(L1[-1:-6:-1])
# Unpacking
num=[1,2,3,9,8,7]
first, *middle, last = num
print("first number =" ,first)
print(middle)
print("last number =" ,last)
              #2
names=["Ahmed","Moho","sara","rehab","Zaky","Abdo","roro"]
first,*others = names
print("the fisrt name is ---->",first)
print(others)
      #3
num=[1,2,3,9,8,7,90,30,60]      
a,*middle,i = num
print(a)
print(middle)
print(i)
      #4
a=10
b=30
a,b = b,a     
# Useful built in function
#len()
names=["Ahmed","Moho","sara","rehab","Zaky","Abdo","roro"]
print(len(names)) # هيقولي سبعة بس ده معناه ان معايا 8 عناصر عشان البايثون بيبتدي بي 0 مش واحد
#index()
print(names.index("Ahmed"))      # هيديني رقمه في اللستة 0 او 1 وهكذا  
#max , min , sum
numbers=[1,2,3,9,8,7,90,30,60]  
print(max(numbers))
print(min(numbers))
print(sum(numbers))
#add and remove 
#append add to the end
numbers=[1,2,3,9,8,7,90,30,60]  
numbers.append(100)
print(numbers)
#extend() add items from anther list
numbers.extend([50])
print(numbers)
#insert
my_list_numbers = [10, 20, 30, 40, 50, 60] 
my_list_numbers.insert(3, 70)
print(my_list_numbers)
#pop() remove and return an Item
l1 = [1, 8, 7, 2, 21, 15]
#l1.pop()
#l1.pop(-1) # == l1.pop()
removed_value = l1.pop(3)
print("I just removed" ,removed_value,"from the list: ", l1)
#count
print("the value 21 appears",l1.count(21),"times in your list")   # how meny times he item appears in list
#sort
l2 = [1, 8, 7, 2, 21, 15, 33]
l3=sorted(l2)
print(l2)
print(l3)
l3[0]=20 # the change js happens in the sorted list
print(l3)
#reverse
l2.reverse() #هيعكس
print(l2) 
#deleting and clearing
#del
del l2[2]
print(l2)
#clear
l2.clear()
print(l2)
#combining and repeating list
a = [1,2,3,4,5]
b = [6,7,8,9,10]
d = [11,12,13,15,14]
c=a+b+d
print(c)
print(c*2)
# Mutability Trap
a = [[]] * 3
a[0] = 3
#a[0].append(5)
print(a)

print(id(a[0]))
print(id(a[1]))
print(id(a[2]))
# nasted lists
a=[20,30,10,[2,3]]
print(a[3][0])
print(a[3][1])
#true or false
b=[1,2,3]
if not b:
    print("B is empty")
else:
    print("B is not empty:")    
print(1 in b)    
print(4 in b)
print(6 not in b)
# copy
l1 = [100,2,34,57,121,787,212]
l2 = l1 # this doesn't creat a copy rather it creats a reference to the same list and if we change one of hem both will gwt changed
l2.append(66)
print(id(l1))
print(id(l2))
l2 = l1.copy()    # it creates a shallow copy and only copies the first level 
l2.append(1000)
print(l1)
print(l2)
b = a.copy() 
a.append(6)
b.append(7)
print(a)
print(b)

a[3].append(3)

print(a)
print(b)
# deep copy
a = [1, 2, 3, [4, 5]]
import copy
b = copy.deepcopy(a)
a[3].append(3)
print(a)
print(b)
