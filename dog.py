class bulldog:
    species = "dog"
    def __init__(self, name, age):
        self.name = name
        self.age = age

poo = bulldog("poodle", 10)
roo = bulldog("retriever", 15)

print("{} is {} years old".format(poo.name, poo.age))
print("{} is {} years old".format(roo.name, roo.age))
