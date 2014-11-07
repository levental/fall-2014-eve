phone_book = {"name": "Sim Lev", "p_num": "999-999-9999", "address": "2717 SE 16th"}

def add():
    a = raw_input("would you like to add an entry" )
    if a == "y":
        name = raw_input("Please add your name")
        p_num = raw_input("please input phone number")
        address = raw_input("please add your address")

def search():
    b = raw_input("Would you like to search? ")
    if b =="y":
        search = raw_input("please insert the first name of the person you are looking for? ")
    if name.has_key(search):
        print "%s is in the dictionary. She is in the DBS" % search
    else:
        print "%s is not in the dictionary" % search

        print (phone_book.keys())

def delete():
    c = raw_input("would you like to delete an entry ")
    if c =="y":
        phone_book.pop(name)

while True:
    ask = raw_input("would you like to add, search, erase or quit? ")
    if ask == "add":
        add()
    elif ask =="search":
        search()
    elif ask == "erase":
        delete()
    elif ask == "quit":
        print "thanks for your time!"
        break
    else:
        print "I did\'t get that, please try again!"







add()
