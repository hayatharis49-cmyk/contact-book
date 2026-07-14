
# Contact Book
# Author: Haris
# Description: A command line contact manager that saves contacts to a CSV file


import csv
import os 

class Contact:
    """Represents a single contact with name, phone and email."""
    
    def __init__(self,name,phone,email):
        """Initialize contact with name, phone and email."""
        self.name = name 
        self.phone = phone 
        self.email = email 
        
    def __str__(self):
        """Return a readable string representation of the contact."""
        return f" Name : {self.name} | Phone :{self.phone} | email :{self.email}"

    def to_list(self):
        """Convert contact to list format for CSV storage."""
        return [self.name,self.phone,self.email]

# Write a function called load_contacts() that:

# Opens contacts.csv in read mode
# Skips the header row
# Returns all rows as a list
# If file doesn't exist returns an empty list




def load_contacts():
    """Load all contacts from contacts.csv"""
    try:
        with open("contacts.csv","r") as f:
            reader=csv.reader(f)
            next(reader)   # skip header row
            contacts_list = list(reader)
        return contacts_list
    except FileNotFoundError:
        # file doesn't exist yet — created on first save
        return []
    


 

# ── Save Function ───────────────────────────
def save_contacts(contact):
    """Save a single contact to contacts.csv"""
    
    # check if file exists before opening to decide if header is needed
    file_exists= os.path.exists("contacts.csv")
    
    with open("contacts.csv","a",newline= "") as f:
        writer=csv.writer(f)
        
        if not file_exists: # write header only if file is being created for first time
            writer.writerow(["name","phone","email"])
            
        writer.writerow(contact.to_list()) # append contact data to end of file
# Write a function called view_contacts() that:
# Loads all contacts using load_contacts()
# If no contacts prints "No contacts yet!"
# Otherwise prints each contact neatly with a number



# ── View Function ────────────────────────────

def view_contacts():
    """Display all contacts from the contact book"""
    # load all contacts from CSV file
    all_contacts = load_contacts()
    if len(all_contacts) == 0:    # check if contact book is empty
        print("no contacts yet")
    else: # print each contact with a number using enumerate
        for index,row in enumerate(all_contacts,start=1):
            print(f"{index}.name : {row[0]} phone :{row[1]} email : {row[2]}")
                

# ── Search Function ──────────────────────────

# Write a function called search_contacts() that:
# Loads all contacts
# Searches for contacts where name matches
# Uses list comprehension to filter
# Prints matching contacts or "No contact found!"


def search_contacts(name):
    # load all contacts from CSV
    contacts = load_contacts()
    # filter contacts using list comprehension — case insensitive search
    results = [row for row in contacts if name.lower() in row[0].lower()]
    if not results:
        print("no contact found")
    else:    # print each matching contact
        for row in results:
            print(f"name : {row[0]} | Phone : {row[1]} | email : {row[2]}")


# ── Delete Function ──────────────────────────

# Write a function called delete_contact() that:
# Loads all contacts
# Filters out the contact with matching name
# Rewrites CSV with remaining contacts
 

def delete_contact(name):
    """Delete a contact by name"""
    # load all contacts from CSV
    contacts = load_contacts()
    result = [row for row in contacts if name.lower() in row[0].lower()]  # check if contact exists
    if not result:
        print("no contact found")
    else:   # keep everyone except the deleted contact
        remaining =[row for row in contacts if not name.lower() in row[0].lower()]
        with open("contacts.csv","w",newline ="") as f:   # rewrite CSV with remaining contacts
            writer = csv.writer(f)
            writer.writerow(["name","phone","email"])  # write header
            writer.writerows(remaining)  # write remaining contacts
        print("contact deleted successfully!")

def main():
    while True:
        print("====== Contact Book ======")
        print("1 for add a contact")
        print("2 for view a contact")
        print("3 for search a contact")
        print("4 for delete a contact")
        print("5 for exit")
        choice = input("write your choice:")
        if choice == "1":
            name=input("write your name :")
            phone = input("write your phone :")
            email =input("write your email :")
            new_contact= Contact(name,phone,email)
            save_contacts(new_contact)
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            name = input("write a name: ")
            search_contacts(name)
        elif choice == "4":
            name= input("write a name :")
            delete_contact(name)
        elif choice == "5":
            print("good bye!")
            break
        else:
            print("invlid choice")
main()
        
            
    
