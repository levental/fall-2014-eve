__author__ = 'simlev81'

raw_data = [
    {
        "name": "Kevin",
        "age" :10
    },
    {
        "name": "Carol",
        "age" :20
    },
    {
        "name": "Ted",
        "age" :43
    }
]

total = 0
index = 0
while total <= 30:
    total += raw_data[index]["age"]
    index+=1
print(index)

def print_all(data):
    for x in data:
        print_detail(person):
        print ("my name is %s and I am %s years old" % (x["name"], x["age"]))
print_all(raw_data)






