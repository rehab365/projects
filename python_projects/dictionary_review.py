my_contact_dictionary = {
   "ehsan":  124,
    "musa": 4124,
    "ahmed": 893,
    "name": "Waseem",
}
print(f"love:{my_contact_dictionary['ahmed']}")
#get In real code, .get() is almost always the safer choice for data 
#you don't fully control
print(f"my_contact_dictionary.get('ahmed'): {my_contact_dictionary.get('ahmed')}\n\n\n\n")
print(f"my_contact_dictionary.get('email'):{my_contact_dictionary.get('email','not found')}")
#adding and updating a key
my_contact_dictionary['email'] = 'rehab@email.com'
print(my_contact_dictionary)
print(f"my_contact_dictionary.get('email):{my_contact_dictionary.get('email')}")
#Removing a Key pop
contact = {"name": "Ahmed", "age": 25, "city": "Karachi"}
#contact.pop("age")
#print(contact)
#del contact["city"]
#print(contact)
#Checking Existence: in / not in
contact = {"name": "Ahmed", "age": 25, "city": "Karachi"}
print("name" in contact)      
print("email" in contact)     
print(25 in contact)  #   (25 is a value, not a key)     
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
# he rest I know I js want to practice more