contacts ={
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9999"

}

print(f"Alice's Number: {contacts["Alice"]}")

contacts["Diana"] = "555-4321" # Adds Diana to the list of contacts. 

print(f"Contacts after adding Diana: {contacts}")

contacts ["Bob"] = "555-0000" # Updates Bob's number in contacts. 

print(f"Contacts after updating Bob: {contacts}")

del contacts["Charlie"] # Deletes the contact "Charlie" from contacts.

print(f"Contacts after deleting Charlie: {contacts}")

print(f"All Names {contacts.keys()}")

print(f"All Numbers {contacts.values()}")

print(f"Total Contacts {len(contacts)}")
