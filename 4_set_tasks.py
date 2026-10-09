#first task
numbers={1,2,3,6,5,20,22,2,22,1,6,7}
print(numbers)
#second task
List=[10,20,30,50,60,30,80,40,44,66,80,70]
print(set(List))

# third task
A={110,220,330}
B={330,440,550} 
print(A|B) # هتطبع كل حاجه بس مش هتكرر
print(A-B)   # هتطبع اللي في ايه بس مش في بي
print(A^B) # هتطبع كل حاجه معدا المشترك

#task
list=["example1@gmail.com","rehab123@gmail.com","mohamed@gmail.com","mohamed@gmail.com"]
list2=["mohamed@gmail.com","hisham@gmail.com","roro235@gmail.com"]
print(set(list|list2))

#task
system_a = ["user1", "user2", "user3", "user4"]
system_b = ["user3", "user4", "user5", "user6"]
print(set(system_a-system_b))
#task
system_b.discard("not_here")