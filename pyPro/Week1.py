#def print_name():
 #   age = 33
  #  first_name = "Simcha"
   # print(first_name + " is " + str(age))

#print_name()


raw_data ={ "name": "Sim", "last_name": "levental", "age": 25 }
def get_response(data):
    template = "Hello %s, how are you, are you the Mr.%s who is %s years old?"
    name = data["name"]
    last_name = data["last_name"]
    age = data["age"]
    result = template % (name, last_name, age)
    return result
response = get_response(raw_data)
print(response)


