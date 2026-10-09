def total(*args):
    #print(type(args))  # tuple
    return sum(args)
print(total(2,6))
print(total(2,9,8,7))


def build_profile(**info): #**kwargs dictionary
    return info
print(build_profile(name="Hisham",age=22))
print(build_profile(user="hisham123",email="hish526@email.com"))


def order(item,*args,**kwargs):
   print(item)
   print(args)
   print(kwargs) 
print(order("book", "pen", "bag", price=50, qty=2))   
#Unpacking — Spreading a List or Dict Into a Call
def greet(name,age):
    print(f"{name} is {age}")
values=["Ahmed",25]
greet(*values)
info={"name":"sara","age":25}
greet(**info)    
#Real-World Use: A Flexible Logging Function
def log(level,*parts,**meta):
    message = "".join(str(p) for p in parts)
    tags = "".join(f"{k}={v}"for k,v in meta.item())
    print(f"[{level}] {message} ({tags})")
log("INFO", "User", "logged in", user_id=42, ip="10.0.0.1")    