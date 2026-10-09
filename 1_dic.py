my_contact_dictionary = {
   "ehsan":  124,
    "musa": 4124,
    "ahmed": 893,
    "name": "Waseem",
}
print(f"my_contact_dictionary['ahmed']: {my_contact_dictionary['ahmed']}")
print(f"my_contact_dictionary.get('ahmed'): {my_contact_dictionary.get('ahmed')}\n\n\n\n")
print(f"my_contact_dictionary.get('email'): {my_contact_dictionary.get('email', 'No Email found')}")
my_contact_dictionary["email"]="ahmed@gmail.com"
print(my_contact_dictionary)
print(f"my_contact_dictionary.get('email'): {my_contact_dictionary.get('email', 'No Email found')}")
del my_contact_dictionary["ahmed"]
print(my_contact_dictionary)
#
print(my_contact_dictionary)
my_contact_dictionary.popitem()
print(my_contact_dictionary)
print("email" in my_contact_dictionary)
print("email" not in my_contact_dictionary)
print("name" not in my_contact_dictionary)
print("name" in my_contact_dictionary)
contact={
    "name":"Ahmed",
    "Age":26,
    "city":"Cairo"
}
for key ,value in contact.items():
    print(key,"->",value)
print(contact.keys())
print(contact.values())
print(contact.items())   
for key in contact.keys():
    print(key)
for val in contact.values():
    print(val)    
    # rea_world use:Aword frequency counter
text = "the cat sat on the mat the cat ran ran ran ran ran I ran very fast you can't catch me"
words = text.split()
counts={}
for word in words:
    if word in counts:
        counts[word]+=1
    else:
       counts[word]=1     
print(counts)       
# nasted dic
user ={
    "name": "Ahmed Ali",
    "address": { "city": "Karachi", "zip": "74200" }
}
print(user['address']['zip'])
#list of dic 
students = [
{"name": "Ahmed", "score": 88},
{"name": "Sara", "score": 92},
{"name": "Bilal", "score": 79},
]
for student in students:
  print(student["name"], "->", student["score"])
# merging dictionaries
defaults = {"theme": "light", "font_size": 12}
user_settings = {"theme": "black"}

# old method
defaults.update(user_settings)
print(defaults) # {'theme': 'light', 'font_size': 16}



merged = defaults | {"font_size": 20}
print(merged)
#setdefault()
counts = {}
counts.setdefault("apple", 0)
counts["apple"] += 1
print(counts) # {'apple': 1}
counts.setdefault("banana", 0)
print(counts) # still {'apple': 1}

