my_info={"name":"Rehab","age":24,"FAV subject":"English"}
print(my_info)
print(f"my_info.get('adress'):{my_info.get('adress')}")
my_info["email"]="rehab@exampil.com"
print(my_info)
for key,value in my_info.items():
    print(key,"---->",value)

text="I love cats cats always are nice"
words=text.split()
counts={}
for word in words:
    if word in counts:
      counts[word]+=1
    else:  
       counts[word]=1
print(counts)     

#anoher tasks 
product = {
    "id": "PROD102",
    "name": "Wireless Mouse",
    "price": 29.99,
    "in_stock": True,
    "tags": ["electronics", "accessory"]
}
product["adress order"]=["cairo street"]
print(product)
del product ["in_stock"]
print(product)
product["name"]=["wire mouse"]

# task

user = {
"name": "Rehab",
"address": { "city": "Giza", "zip": "506030" }
}
print(user["address"]["zip"]) 

